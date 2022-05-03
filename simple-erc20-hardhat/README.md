# Simple ERC20 contract deployment
This directory contains all the files necessary to deploy simplest ERC20-like contract using Neon onto the Solana blockchain.

# Requirements
You should have **nodejs** and **npm** package manager installed on your system

# Preparing
## Setup Neon account (using Metamask)
**NOTE: Currently Metamask plugin for Firefox not working with Neon, please use another browser**
- Connect your metamask wallet to Neon Devnet using these settings:
    - Network Name: Neon Devnet
    - New RPC URL: https://proxy.devnet.neonlabs.org/solana
    - Chain ID: 245022926
    - Currency Symbol (optional): NEON
- Create new account in Metamask
- Airdrop at most 100 NEONs to just created account [from here](https://neonfaucet.org/)
- Copy your Metamask account private key (Account Details >> Export Private Key)
- Insert just copied private key into quotes in line 5 in file **hardhat.config.js** - **NOTE** Add **0x** prefix in beginning

# Running example
1. Change current directory to simple-erc20. All the next steps will be executed considering this is your current directory.
2. Install NPM packages:
    > npm i
3. Compile contracts with hardhat:
    > npx hardhat compile
4. Deploy ERC20 contract:
    > npx hardhat run ./scripts/deploy.js

After this step you will get output like:

> Deploying contracts with the account: 0xcB31Ce6E4Ff9E2C8f6CbB7044dd9529263a846De
>
> Contract address is:  0x66eCCEe29F6FbDb055379A557f8fb7716964dF1a
>
> Minting  100000000000  tokens...
>
> Balance of deployer is:  BigNumber { value: "100000000000" }

5. Copy contract address got on the previous step and import it as an asset into Metamask (see https://metamask.zendesk.com/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask for help)