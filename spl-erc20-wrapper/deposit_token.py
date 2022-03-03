from erc20_wrapper import ERC20Wrapper
from common import *
import sys

ERC20_CONTRACT_ADDRESS = sys.argv[1]
AMOUNT = int(sys.argv[2])

print(f'Deposit {AMOUNT} tokens {TEST_TOKEN_MINT} wrapped with {ERC20_CONTRACT_ADDRESS} to {neon_account.address}')

wrapper = ERC20Wrapper(
    solana_client,
    neon_client,
    TEST_TOKEN_MINT,
    ERC20_CONTRACT_ADDRESS,
    None) #interface not used here

wrapper.deposit(solana_account, neon_account.address, AMOUNT)