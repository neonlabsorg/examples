from brownie import ERC20ForSplFactory

from . import utils


def main():
    spl_erc20_contract = utils.SplERC20Brownie(ERC20ForSplFactory)
