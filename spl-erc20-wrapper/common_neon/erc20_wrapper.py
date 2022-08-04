from solcx import install_solc
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID
from eth_account.signers.local import LocalAccount as NeonAccount
from solana.rpc.api import Account as SolanaAccount
from solana.publickey import PublicKey
from solana.transaction import AccountMeta, TransactionInstruction
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY
from solana.rpc.types import TxOpts, RPCResponse, Commitment
import spl.token.instructions as spl_token
from typing import Union, Dict
import struct
from logged_groups import logged_group
from .compute_budget import TransactionWithComputeBudget
from sha3 import keccak_256
from .eth_proto import Trx
from .neon_instruction import NeonIxBuilder
from .web3 import NeonWeb3
from .address import EthereumAddress
import os
import json

install_solc(version='0.7.6')
from solcx import compile_source

@logged_group("neon.Proxy")
class ERC20Wrapper:
    proxy: NeonWeb3
    name: str
    symbol: str
    token: Token
    evm_loader_id: PublicKey
    interface: Dict
    wrapper: Dict

    def __init__(self, 
                 proxy: NeonWeb3,
                 token: Token,
                 evm_loader_id: PublicKey,
                 contract):
        self.proxy = proxy
        self.token = token
        self.evm_loader_id = evm_loader_id
        self.contract = contract

    def get_neon_account_address(self, neon_account_address: str) -> PublicKey:
        neon_account_addressbytes = bytes.fromhex(neon_account_address[2:])
        return PublicKey.find_program_address([b"\1", neon_account_addressbytes], self.evm_loader_id)[0]

    @staticmethod
    def from_address(proxy: NeonWeb3,
                     token: Token,
                     evm_loader_id: PublicKey,
                     contract_address: str):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "ERC20ForSpl.json"
        abi_path = os.path.join(script_dir, rel_path)

        with open(abi_path, 'r') as file:
            source = file.read()
        abi = json.loads(source)
        contract = proxy.eth.contract(address=contract_address, abi=abi['abi'], bytecode=abi['bytecode'])

        return ERC20Wrapper(proxy, token, evm_loader_id, contract)
        
    @staticmethod
    def deploy_wrapper(proxy: NeonWeb3,
                       token: Token,
                       evm_loader_id: PublicKey,
                       name: str, 
                       symbol: str, 
                       payer: NeonAccount):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "erc20_for_spl.sol"
        wrapper_path = os.path.join(script_dir, rel_path)

        with open(wrapper_path, 'r') as file:
            source = file.read()
        compiled_wrapper = compile_source(source)
        wrapper = compiled_wrapper["<stdin>:ERC20ForSpl"]

        contract = proxy.eth.contract(abi=wrapper['abi'], bytecode=wrapper['bin'])
        nonce = proxy.eth.get_transaction_count(proxy.eth.default_account)
        tx = {'nonce': nonce}
        tx_constructor = contract.constructor(name, symbol, bytes(token.pubkey)).buildTransaction(tx)
        tx_deploy = proxy.eth.account.sign_transaction(tx_constructor, payer.key)
        tx_deploy_hash = proxy.eth.send_raw_transaction(tx_deploy.rawTransaction)
        tx_deploy_receipt = proxy.eth.wait_for_transaction_receipt(tx_deploy_hash)
        contract.address = tx_deploy_receipt.contractAddress

        return ERC20Wrapper(proxy, token, evm_loader_id, contract)

    def get_neon_erc20_account_address(self, neon_account_address: str):
        neon_contract_address_bytes = bytes.fromhex(self.contract.address[2:])
        neon_account_address_bytes = bytes.fromhex(neon_account_address[2:])
        seeds = [b"\1", b"ERC20Balance",
                 bytes(self.token.pubkey),
                 neon_contract_address_bytes,
                 neon_account_address_bytes]
        return PublicKey.find_program_address(seeds, self.evm_loader_id)[0]

    def create_associated_token_account(self, owner: PublicKey, payer: SolanaAccount):
        # Construct transaction
        # This part of code is based on original implementation of Token.create_associated_token_account
        # except that skip_preflight is set to True
        tx = TransactionWithComputeBudget()
        create_ix = spl_token.create_associated_token_account(
            payer=payer.public_key(), owner=owner, mint=self.token.pubkey
        )
        tx.add(create_ix)
        self.token._conn.send_transaction(tx, payer, opts=TxOpts(skip_preflight = True, skip_confirmation=False))
        return create_ix.keys[1].pubkey

    def create_claim_instruction(self, owner: PublicKey, from_acc: PublicKey, to_acc: NeonAccount, amount: int):
        nonce = self.proxy.eth.get_transaction_count(to_acc.address)
        claim_tx = self.contract.functions.claim(bytes(from_acc), amount).buildTransaction({'nonce': nonce, 'gasPrice': 0})
        claim_tx = self.proxy.eth.account.sign_transaction(claim_tx, to_acc.key)

        eth_trx = bytearray.fromhex(claim_tx.rawTransaction.hex()[2:])
        emulating_result = self.proxy.neon.emulate(eth_trx)

        eth_accounts = dict()
        for account in emulating_result['accounts']:
            key = account['account']
            eth_accounts[key] = AccountMeta(pubkey=PublicKey(key), is_signer=False, is_writable=True)
            if account['contract']:
                key = account['contract']
                eth_accounts[key] = AccountMeta(pubkey=PublicKey(key), is_signer=False, is_writable=True)

        for account in emulating_result['solana_accounts']:
            key = account['pubkey']
            eth_accounts[key] = AccountMeta(pubkey=PublicKey(key), is_signer=False, is_writable=True)

        eth_accounts = list(eth_accounts.values())

        neon = NeonIxBuilder(owner)
        neon.init_operator_ether(EthereumAddress(to_acc.address))
        neon.init_eth_tx(Trx.fromString(eth_trx))
        neon.init_eth_accounts(eth_accounts)
        return neon

    def create_input_liquidity_instruction(self, payer: PublicKey, from_address: PublicKey, to_address: str, amount: int):
        return TransactionInstruction(
            program_id=TOKEN_PROGRAM_ID,
            data=b'\3' + struct.pack('<Q', amount),
            keys=[
                AccountMeta(pubkey=from_address, is_signer=False, is_writable=True),
                AccountMeta(pubkey=self.get_neon_erc20_account_address(to_address), is_signer=False, is_writable=True),
                AccountMeta(pubkey=payer, is_signer=True, is_writable=False)
            ]
        )

    def mint_to(self, destination: Union[PublicKey, str], amount: int, mint_authority: SolanaAccount) -> RPCResponse:
        """
        Method mints given amount of tokens to a given address - either in NEON or Solana format
        NOTE: destination account must be previously created
        """
        if isinstance(destination, str):
            destination = self.get_neon_erc20_account_address(destination)
        return self.token.mint_to(destination, mint_authority, amount,
                                  opts=TxOpts(skip_preflight=True, skip_confirmation=False))

    def erc20_interface(self):
        return self.contract

    def get_balance(self, address: Union[PublicKey, str]) -> int:
        if isinstance(address, PublicKey):
            return int(self.token.get_balance(address, Commitment('confirmed'))['result']['value']['amount'])

        return self.contract.functions.balanceOf(address).call()
