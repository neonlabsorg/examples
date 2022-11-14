import os
import random
import string

from brownie import ERC20ForSplMintable as contract_factory
from brownie import network

from .utils import Faucet

FAUCET_URL = os.environ["FAUCET_URL"]


def deploy_from_factory(
    account: network.account.LocalAccount,
    contract_factory: network.contract.ContractContainer,
) -> network.contract.ProjectContract:
    """Deploy contract from factory"""
    if not isinstance(account, str):
        account = account.address
    symbol = "".join(random.sample(string.ascii_uppercase, 3))
    contract_name = f"spl erc20 {symbol}"
    print(f"deploy `ERC20` contract")
    contract = contract_factory.deploy(
        contract_name, symbol, 18, account, {"from": account}
    )
    print(f"contract deployed `{contract.address}`")
    return contract


def main():
    amount = pow(10, 4)
    sender = os.environ.get("ACC1") or network.accounts.add()
    Faucet(FAUCET_URL).request_neon(sender.address)
    print(f"{sender.address} Neon balance `{sender.balance()}`")
    recipient = os.environ.get("ACC2") or network.accounts.add()
    contract = deploy_from_factory(sender, contract_factory)
    print(f"mint amount `{amount}`")
    contract.mint(sender.address, amount, {"from": sender.address})
    print(f"{sender.address[:10]} erc20 balance `{contract.balanceOf(sender.address)}`")
    print(f"transfer tokens from `{sender.address[:10]}` to `{recipient.address[:10]}`")
    contract.transfer(recipient.address, 100, {"from": sender.address})
    print(f"{sender.address[:10]} erc20 balance `{contract.balanceOf(sender.address)}`")
    print(
        f"{recipient.address[:10]} erc20 balance `{contract.balanceOf(recipient.address)}`"
    )
