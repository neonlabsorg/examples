from erc20_wrapper import ERC20Wrapper
from common import *
import sys

ERC20_CONTRACT_ADDRESS = sys.argv[1]
AMOUNT = int(sys.argv[2])

interface_abi = None
with open('./erc20_iface.json', 'r') as f:
    interface_abi = json.load(f)

wrapper = ERC20Wrapper(
    solana_client,
    neon_client,
    TEST_TOKEN_MINT,
    ERC20_CONTRACT_ADDRESS,
    interface_abi)

wrapper.withdraw(neon_account, solana_account.public_key(), AMOUNT, solana_account)