from brownie import accounts, network, ERC20

## add account: brownie accounts new my_account
### accounts.load("my_account")

def deploy_erc20():
    #
    account = get_account()
    erc_contract = ERC20.deploy({"from":account})
    print(f"erc contract is: {erc_contract}")
    amount = (100 * 10 ** 9)
    mint_tx = erc_contract.mint(amount)
    print(f"minting...{amount}")
    mint_tx.wait(1)
    
   
def get_account():
    return accounts.load("neon_dev")

def main():
    deploy_erc20()
