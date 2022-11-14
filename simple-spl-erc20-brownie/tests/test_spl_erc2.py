# coding: utf-8
import os
import random
import string

import pytest
from brownie import ERC20ForSplMintable as contract_factory
from brownie import network

from scripts.utils import Faucet

FAUCET_URL = os.environ["FAUCET_URL"]


@pytest.fixture(scope='session')
def faucet() -> Faucet:
    return Faucet(FAUCET_URL)


@pytest.fixture(scope="session")
def sender(faucet: Faucet) -> network.account.LocalAccount:
    """Create tokens sender account"""
    account = network.accounts.add()
    print(f"request neon for {account.address[:10]}")
    amount = pow(10, 3)
    faucet.request_neon(account.address, amount)
    return account


@pytest.fixture(scope="session")
def recipient() -> network.account.LocalAccount:
    """Create recipient account"""
    return network.accounts.add()


@pytest.fixture(scope="session")
def contract(
    sender: network.account.LocalAccount,
) -> network.contract.ProjectContract:
    """Deploy contract from factory"""
    if not isinstance(sender, str):
        account = sender.address
    symbol = "".join(random.sample(string.ascii_uppercase, 3))
    contract_name = f"spl erc20 {symbol}"
    print(f"deploy `ERC20` contract")
    contract = contract_factory.deploy(
        contract_name, symbol, 18, account, {"from": account}
    )
    print(f"contract deployed `{contract.address}`")
    amount = pow(10, 4)
    print(f"mint amount `{amount}`")
    contract.mint(account, amount, {"from": account})
    assert contract.balanceOf(account) == amount
    return contract


def test_token_transfer(
    contract: network.contract.ProjectContract,
    sender: network.account.LocalAccount,
    recipient: network.account.LocalAccount,
) -> None:
    """Check tokens transfer"""
    amout = 100
    neon_balance = sender.balance()
    erc20_balance = contract.balanceOf(sender.address)
    print(f"transfer tokens from `{sender.address[:10]}` to `{recipient.address[:10]}`")
    contract.transfer(recipient.address, amout, {"from": sender.address})
    assert contract.balanceOf(recipient.address) == amout
    assert contract.balanceOf(sender.address) == erc20_balance - amout
    assert sender.balance() < neon_balance
