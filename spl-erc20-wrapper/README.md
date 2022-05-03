# Example of wrapping SPL token by ERC-20 interface in Neon

## Requirements

  - [Install solana CLI to your computer](https://docs.solana.com/ru/cli/install-solana-cli-tools)
  - [Install SPL Token program](https://spl.solana.com/token). If you are using one of Linux distributions you will probably should install packets: gcc, libudev-dev, libssl-dev. 
  - python3 and pip3 installed
  - install python requirements:
    
    > pip3 install -r requirements.txt

  - npm package manager if you'd like to deploy contracts using hardhat

## Setup Solana account

- Make sure you are on devnet solana:
  > solana config get
  
  RPC URL should be https://api.devnet.solana.com

  Evaluate command if not:
  > solana config set --url devnet 

- Create new solana account. You will be asked for passphrase (may skip this step by pressing Enter)
  > solana-keygen new -o ~/.config/solana/id.json --force

- Airdrop SOLs to just created account:
  > solana airdrop 2

## Setup Neon account (using Metamask)
**NOTE: Currently Metamask plugin for Firefox not working with Neon, please use another browser**
- Connect your metamask wallet to Neon Devnet using this settings:
    - Network Name: Neon Devnet
    - New RPC URL: https://proxy.devnet.neonlabs.org/solana
    - Chain ID: 245022926
    - Currency Symbol (optional): NEON
- Create new account in Metamask
- Airdrop at most 100 NEONs to just created account [from here](https://neonfaucet.org/)
- Copy your Metamask account private key (Account Details >> Export Private Key)
- Insert just copied private key into quotes in line 15 in file **common.py**
- Insert just copied private key into quotes in line 5 in file **hardhat.config.js** - **NOTE** Add **0x** prefix in begining

## Create new token mint

- Change current directory to spl-erc20-wrapper

- Generate keypair for new SPL token:
  > solana-keygen new -o test-token-mint.json --force
  
  You will be asked for passphrase (may skip this step by pressing Enter)
  test-token-mint.json file now contains private key of your SPL token. Now we will extract it's public key to environment variable using solana tool:
  > export AWESOME_TOKEN_ADDRESS=$(solana address -k test-token-mint.json)

- Create new SPL token by running command:
  > spl-token -u devnet create-token -- test-token-mint.json

## Creating ERC20 wrapper

### First way: Using python script

- Run deploy_wrapper.py script 
  > export WRAPPER_ADDRESS=$(python3 deploy_wrapper.py)

- Import just created token into Metamask. You can get it's address by command:
  > echo $WRAPPER_ADDRESS

### Second way: Using hardhat

- Install JS requirements:
  > npm i

- Compile contract
  > npx hardhat compile

- Deploy contract
  > export WRAPPER_ADDRESS=$(npx hardhat run --network neonlabs scripts/deploy.js)
  
- Import just created token into Metamask. You can get it's address by command:
  > echo $WRAPPER_ADDRESS
  
## Minting tokens

- Create associated token account using token mint address got on previous step:
  > spl-token -u devnet create-account $AWESOME_TOKEN_ADDRESS

  After succesfull execution of this command you will get address of your new token account and signature of the transaction

- Mint some tokens to just created wallet:
  > spl-token -u devnet mint $AWESOME_TOKEN_ADDRESS 1000

- Check balance
  > spl-token -u devnet balance $AWESOME_TOKEN_ADDRESS

## Depositing SPL tokens from Solana into Neon

- Run deposit_token.py with two arguments:
  - address of ERC20 wrapper got on step 'Creating ERC20 wrapper'
  - amount
  > python3 deposit_token.py $WRAPPER_ADDRESS 10000000000

## Withdrawing ERC20-wrapped SPL tokens from Neon to Solana

- Run withdraw_token.py with two arguments:
  - address of ERC20 wrapper got on step 'Creating ERC20 wrapper'
  - amount
  > python3 withdraw_token.py $WRAPPER_ADDRESS 1000000000
