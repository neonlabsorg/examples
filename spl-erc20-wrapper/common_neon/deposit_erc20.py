from .erc20_wrapper import ERC20Wrapper
from .compute_budget import TransactionWithComputeBudget
from solana.publickey import PublicKey as SolanaPublicKey
from solana.account import Account as SolanaAccount
from eth_keys.datatypes import PrivateKey as NeonPrivateKey
from eth_account.signers.local import LocalAccount as NeonAccount
from .environment_data import EVM_LOADER_ID
import spl.token.instructions as SplTokenInstrutions
from solana.transaction import TransactionInstruction, AccountMeta
from .neon_instruction import create_account_layout
from solana.system_program import SYS_PROGRAM_ID
from spl.token.client import Token as SplToken
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.rpc.types import TxOpts

import sys
from spl.token.instructions import get_associated_token_address

def get_evm_loader_account_address(eth_address: str):
    eth_addressbytes = bytes.fromhex(eth_address[2:])
    return SolanaPublicKey.find_program_address([b"\1", eth_addressbytes], SolanaPublicKey(EVM_LOADER_ID))

class TokenGate:
    def __init__(self, solana, neon_proxy, token_mint, wrapper_address):
        self.solana = solana
        self.proxy = neon_proxy
        self.token = SplToken(self.solana, token_mint, TOKEN_PROGRAM_ID, None)
        self.wrapper = ERC20Wrapper.from_address(self.proxy, self.token, SolanaPublicKey(EVM_LOADER_ID), wrapper_address)

    def create_account_instruction(self, eth_address: str, payer: SolanaPublicKey):
        dest_address_solana, nonce = get_evm_loader_account_address(eth_address)
        print(f'dest_address_solana = {dest_address_solana}')
        print(f'payer = {payer}')
        return TransactionInstruction(
            program_id=SolanaPublicKey(EVM_LOADER_ID),
            data=create_account_layout(bytes.fromhex(eth_address[2:]), nonce),
            keys=[
                AccountMeta(pubkey=payer, is_signer=True, is_writable=True),
                AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
                AccountMeta(pubkey=dest_address_solana, is_signer=False, is_writable=True),
            ])

    def deposit_erc20(self, sender: SolanaAccount, receiver: NeonAccount):
        print(f'token.pubkey = {self.token.pubkey}')
        from_spl_token_acc = get_associated_token_address(sender.public_key(), self.token.pubkey)

        print(f'        OWNER {sender.public_key()}')
        print(f'            SPL TOKEN ACC {from_spl_token_acc}')
        print(f'            RECEIVER: {receiver.address}')

        TRANSFER_AMOUNT = 123456
        trx = TransactionWithComputeBudget()

        acct_info = self.solana.get_account_info(get_evm_loader_account_address(receiver.address))
        if acct_info is None:
            trx.add(self.create_account_instruction(receiver.address, sender.public_key()))

        print(f"program_id = {self.token.program_id}")
        print(f"source = {from_spl_token_acc}")
        print(f"delegate = {self.wrapper.get_neon_account_address(receiver.address)}")
        print(f"owner = {sender.public_key()}")
        print(f"amount = {TRANSFER_AMOUNT}")

        trx.add(SplTokenInstrutions.approve(SplTokenInstrutions.ApproveParams(
            program_id=self.token.program_id,
            source=from_spl_token_acc,
            delegate=self.wrapper.get_neon_account_address(receiver.address),
            owner=sender.public_key(),
            amount=TRANSFER_AMOUNT,
            signers=[],
        )))
        claim_instr = self.wrapper.create_claim_instruction(
            owner = sender.public_key(),
            from_acc=from_spl_token_acc, 
            to_acc=receiver,
            amount=TRANSFER_AMOUNT,
        )
        trx.add(claim_instr.make_noniterative_call_transaction(len(trx.instructions)))

        opts = TxOpts(skip_preflight=True, skip_confirmation=False)
        print(self.solana.send_transaction(trx, sender, opts=opts))
    
