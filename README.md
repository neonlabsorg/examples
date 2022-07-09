# Examples
- **simple-erc20-hardhat** - deploying simple ERC20 token contract using Hardhat. This token can 'live' only inside Neon
- **simple-erc20-truffle** - deploying simple ERC20 token contract using Truffle. This token can 'live' only inside Neon
- **simple-erc20-brownie** - deploying simple ERC20 token contract using python and brownie. This token can 'live' only inside Neon
- **spl-erc20-wrapper** - creating SPL token in Solana and deploying ERC20-wrapper contract to interact with SPL token from Neon

# Running local environment
Examples uses neon-devnet by default but you can also run your own setup locally for testing and experiments. Install latest docker and docker-compose. Make sure you have the latest version of docker-compose installed. It's v2.6.1 at the time of this update. To install v2.6.1, first remove existing installation of docker-compose:

```bash
sudo apt remove docker-compose
```

then install v2.6.1 wiht the following commands:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```


Then check the version to make sure it is the right one:

```bash
docker-compose --version   
```

you shoud see

```Docker Compose version v2.6.1 ```


**NOTE** local setup is only available on Linux OS-es. Just run from this directory:

```bash
docker-compose up -d
```

All APIs will be available at your localhost by addresses:

- solana **http://localhost:8899**
- faucet **http://localhost:3333**
- web3 proxy (Eth API) - **http://localhost:9090/solana**

## Airdropping in local environment

Just execute from this directory:

```bash
./drop_neons.sh &lt;target-eth-address>
```

**NOTE** Make sure you have **curl** installed in your system
