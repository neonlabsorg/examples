# Example deploying ERC20 to Neonlabs devnet using Hardhat

This directory contains all the files necessary to deploy simplest ERC20-like contract using Neon onto the Solana blockchain.

## Cloning repository

Run command

```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/simple-erc20-hardhat** directory

## Installing requirements

1. Install requirements

```sh
npm install
```

**NOTE** In case of error try to execute:

```sh
npm cache clear --force
```

and then back to previous command

## Setup Neon account (using Metamask)

**NOTE** Private keys in **hardhat.config.js** file are compromised so it is highly recommended to setup your own test
accounts to run this example. This project uses two test accounts. We will call it **account #1** and **account #2**
To create new accounts:

1. Setup your Metamask wallet to work with Neon devnet:

   - Connect your metamask wallet to Neon Devnet using these settings:
     - Network Name: Neon Devnet
     - New RPC URL: https://devnet.neonevm.org
     - Chain ID: 245022926
     - Currency Symbol (optional): NEON

2. Create 2 new accounts in Metamask
3. Airdrop at most 100 NEONs to just created **account #1** [from here](https://neonfaucet.org/)
4. Copy your Metamask account's private keys (Account Details >> Export Private Key) and insert them into **hardhat.config.js**
   at lines 9 (**account #1**) and line 10 (**account #2**) **NOTE!** Add **0x** prefix at the beginning

## Running tests on devnet

Execute command

```sh
npx hardhat test
```

This command will do next:

1. Compile all smart-contracts related to this project
2. Deploy these smart-contracts to the Neon devnet
3. Run tests from ./test/test_erc20.js

After successfully running this step you should get console output similar to:

```sh
Compiled 2 Solidity files successfully


  Testing TestERC20 contract
    ✔ should successfully mint 10000 ERC20 in the first account (15967ms)
    ✔ should transfer token correctly (31327ms)


  2 passing (53s)

```

## Compiling and deploying contract

1. Compiling contract

```sh
npx hardhat compile
```

3. Deploying contract

```sh
npx hardhat run ./scripts/deploy.js
```

After successfully running this step you should get console output similar to:

```sh
Deploying contracts with the account: 0xf71c4DACa893E5333982e2956C5ED9B648818376
Contract address is:  0x49DCDEc367bba4271876259AE473890aa5AABc2e
Minting  100000000000  tokens...

```

This project contains only one deployment script which performs two actions:

1. Deploying test ERC20 smart-contract
2. Minting 100000000000 TERC20 token
   to **account #1** specified in **hardhat.config.js** file on line 9

In migration command output, in the line `Contract address is: 0x49DCDEc367bba4271876259AE473890aa5AABc2e` is our
new ERC20 token contract address. You can easily import it into your Metamask wallet. After it you can transfer new
token from previously created **account #1**

## ...Try it with your own contract and have fun!
