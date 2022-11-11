# coding: utf-8
import os
import random
import string
import typing as tp

import requests
from brownie import ERC20ForSplFactory
from brownie import network

try:
    FAUCET_URL = os.environ["FAUCET_URL"]
except KeyError as e:
    e.args = (
        "Please create .env file and paste `export FAUCET_URL=your_faucet_url` to it",
    )
    raise


class Faucet:
    def __init__(self, faucet_url: str, session: tp.Optional[tp.Any] = None) -> None:
        self._url = faucet_url
        self._session = session or requests.Session()

    def request_neon(
        self, account: network.account.LocalAccount, amount: int = 1000
    ) -> None:
        response = self._session.post(
            self._url, json={"amount": amount, "wallet": account.address}
        )
        response.raise_for_status()


class SplERC20Brownie:
    """Implements base SPL ERC20 pipeline"""

    def __init__(
        self, account: tp.Optional[network.account.LocalAccount] = None
    ) -> None:
        self._account = account or network.accounts.add()
        self._faucet = Faucet(FAUCET_URL)
        self._faucet.request_neon(self._account)
        self._contract = self._deploy_from_factory(ERC20ForSplFactory)

    def _deploy_from_factory(
        self, contract_factory: network.contract.ContractContainer
    ) -> network.contract.ProjectContract:
        """Deploy contract from factory"""
        contract = contract_factory.deploy({"from": self._account.address})
        symbol = "".join(random.sample(string.ascii_uppercase, 3))
        instruction_tx = contract.createErc20ForSplMintable(
            "SPL ERC20 test", symbol, 18, self._account.address
        )
        return contract

    #
    # account = get_account()
    # erc_contract = ERC20.deploy({"from": account})
    # print(f"erc contract is: {erc_contract}")
    # amount = 100 * 10 ** 9
    # mint_tx = erc_contract.mint(amount)
    # print(f"minting...{amount}")
    # mint_tx.wait(1)
