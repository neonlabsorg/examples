from erc20_wrapper import ERC20Wrapper
from common import *

wrapper = ERC20Wrapper.deploy(
    'Awesome Token', 
    'AWST', 
    solana_client,
    neon_client,
    TEST_TOKEN_MINT,
    neon_account)

print(f'{wrapper.eth_contract_address}')