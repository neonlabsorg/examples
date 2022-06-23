# Examples
- **simple-erc20-hardhat** - deploying simple ERC20 token contract using Hardhat. This token can 'live' only inside Neon
- **simple-erc20-truffle** - deploying simple ERC20 token contract using Truffle. This token can 'live' only inside Neon
- **spl-erc20-wrapper** - creating SPL token in Solana and deploying ERC20-wrapper contract to interact with SPL token from Neon

# Running local environment
Examples uses neon-devnet by default but you can also run your own setup locally for testing and experiments. Install latest docker and docker-compose. **NOTE** local setup is only available on Linux OS-es. Just run from this directory:

> docker-compose up -d

All APIs will be available at your localhost by addresses:

- solana **http://localhost:8899**
- faucet **http://localhost:3333**
- web3 proxy (Eth API) - **http://localhost:9090/solana**

## Airdropping in local environment

Just execute from this directory:

> ./drop_neons.sh &lt;target-eth-address>

**NOTE** Make sure you have **curl** installed in your system
