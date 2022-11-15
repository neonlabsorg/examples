# coding: utf-8
import os
import random
import string

import pytest
from brownie import ERC20ForSplMintable as contract_factory
from brownie import network

from scripts.utils import Faucet

FAUCET_URL = os.environ["FAUCET_URL"]


@pytest.fixture(scope="session", autouse=True)
def faucet() -> Faucet:
    return Faucet(FAUCET_URL)


@pytest.fixture(scope="session", autouse=True)
def contract_symbol() -> str:
    """Generate random string"""
    return "".join(random.sample(string.ascii_uppercase, 3))


@pytest.fixture(scope="session", autouse=True)
def contract_name(contract_symbol: str) -> str:
    """Generate contract name"""
    return f"spl erc20 {contract_symbol}"


@pytest.fixture(scope="session", autouse=True)
def random_decimals(contract_symbol: str) -> str:
    """Generate random int"""
    return random.randint(10, 25)


@pytest.fixture(scope="session", autouse=True)
def sender(faucet: Faucet) -> network.account.LocalAccount:
    """Create tokens sender account"""
    account = network.accounts.add()
    print(f"request neon for {account.address[:10]}")
    amount = pow(10, 3)
    faucet.request_neon(account.address, amount)
    assert account.balance()
    return account


@pytest.fixture(scope="session")
def recipient() -> network.account.LocalAccount:
    """Create recipient account"""
    return network.accounts.add()


@pytest.fixture(scope="session")
def contract(
    sender: network.account.LocalAccount,
    contract_symbol: str,
    contract_name: str,
    random_decimals: int,
) -> network.contract.ProjectContract:
    """Deploy contract from factory"""
    if not isinstance(sender, str):
        account = sender.address
    print(f"deploy `ERC20` contract")
    contract = contract_factory.deploy(
        contract_name, contract_symbol, random_decimals, account, {"from": account}
    )
    print(f"contract deployed `{contract.address}`")
    amount = pow(10, 4)
    print(f"mint amount `{amount}`")
    contract.mint(account, amount, {"from": account})
    assert contract.balanceOf(account) == amount
    return contract


def test_check_name(
    contract: network.contract.ProjectContract, contract_name: str
) -> None:
    """Check contract name is valid"""
    assert contract.name() == contract_name


def test_check_symbol(
    contract: network.contract.ProjectContract, contract_symbol: str
) -> None:
    """Check contract symbol is valid"""
    assert contract.symbol() == contract_symbol


def test_check_decimals(
    contract: network.contract.ProjectContract, random_decimals: int
) -> None:
    """Check contract decimals is valid"""
    assert contract.decimals() == random_decimals


def test_check_burn(
    contract: network.contract.ProjectContract, sender: network.account.LocalAccount
) -> None:
    """Check contract burn is work"""
    amount = 1
    balance = contract.balanceOf(sender.address)
    tx = contract.burn(amount, {"from": sender.address})
    assert not tx.error()
    assert dict(tx.events)["Transfer"]["amount"] == amount
    assert contract.balanceOf(sender.address) == balance - amount


def test_check_approve(
    contract: network.contract.ProjectContract, sender: network.account.LocalAccount
) -> None:
    """Check contract approve is work"""
    amount = 1
    balance = contract.balanceOf(sender.address)
    tx = contract.approve(sender.address, amount, {"from": sender.address})
    assert not tx.error()
    assert dict(tx.events)["Approval"]["amount"] == amount
    assert contract.balanceOf(sender.address) == balance


def test_check_total_supply(
    contract: network.contract.ProjectContract, sender: network.account.LocalAccount
) -> None:
    """Check contract totalSupply is work"""
    amount = 1
    final_argumet = {"from": sender.address}
    total_supply = contract.totalSupply(final_argumet)
    tx = contract.burn(amount, final_argumet)
    assert not tx.error()
    assert contract.totalSupply(final_argumet) == total_supply - amount


def test_token_transfer(
    contract: network.contract.ProjectContract,
    sender: network.account.LocalAccount,
    recipient: network.account.LocalAccount,
) -> None:
    """Check tokens transfer"""
    amount = 1
    neon_balance = sender.balance()
    erc20_balance = contract.balanceOf(sender.address)
    print(f"transfer tokens from `{sender.address[:10]}` to `{recipient.address[:10]}`")
    tx = contract.transfer(recipient.address, amount, {"from": sender.address})
    assert not tx.error()
    assert dict(tx.events)["Transfer"]["amount"] == amount
    assert contract.balanceOf(recipient.address) == amount
    assert contract.balanceOf(sender.address) == erc20_balance - amount
    assert sender.balance() < neon_balance
