# Example deploying ERC20 to Neonlabs devnet using Truffle

## Cloning repository
Run command
```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/simple-erc20-truffle** directory

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

**NOTE** Private keys in **truffle-config.js** file are compromised so it is highly recommended to setup your own test 
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
4. Copy your Metamask account's private keys (Account Details >> Export Private Key) and insert them into **truffle-config.js** 
    at lines 11 (**account #1**) and line 12 (**account #2**) **NOTE!** Add **0x** prefix at the beginning

## Running tests on denvet

Execute command

```sh
./node_modules/.bin/truffle test --network neonlabs
```

This command will do next:
1. Compile all smart-contracts related to this project
2. Deploy these smart-contracts to the Neon devnet
3. Run tests from ./test/test_erc20.js

After successfully running this step you should get console output similar to:
```sh
Using network 'neonlabs'.


Compiling your contracts...
===========================
✔ Fetching solc version list from solc-bin. Attempt #1
✔ Downloading compiler. Attempt #1.
✔ Fetching solc version list from solc-bin. Attempt #1
> Compiling ./contracts/ERC20.sol
> Compiling ./contracts/IERC20.sol
> Artifacts written to /tmp/test--947955-ciBGiafT1chM
> Compiled successfully using:
   - solc: 0.8.16+commit.07a7930e.Emscripten.clang


  Contract: TestERC20
    ✓ should successfully mint 10000 ERC20 in the first account (5288ms)
    ✓ should transfer token correctly (7335ms)


  2 passing (13s)

```

## Compiling and deploying contract

1. Compiling contract
```sh
./node_modules/.bin/truffle compile
```
3. Deploying contract
```sh
./node_modules/.bin/truffle migrate --network neonlabs
```

After successfully running this step you should get console output similar to:

```sh
Compiling your contracts...
===========================
✔ Fetching solc version list from solc-bin. Attempt #1
✔ Fetching solc version list from solc-bin. Attempt #1
> Everything is up to date, there is nothing to compile.


Starting migrations...
======================
> Network name:    'neonlabs'
> Network id:      245022926
> Block gas limit: 260057650590124 (0xec8563e271ac)


1_erc20.js
==========

   Deploying 'ERC20'
   -----------------
   > transaction hash:    0x54db68667335ab2c6e8aeee1080b30ac39209186e2f0c12dba97b7130d923382
   > Blocks: 11           Seconds: 4
   > contract address:    0x7364DA3a4989898Ac2d466611Ce4b957885DF7B8
   > block number:        158638454
   > block timestamp:     1661872308
   > account:             0xf71c4DACa893E5333982e2956C5ED9B648818376
   > balance:             8.205758048453800748
   > gas used:            43936740 (0x29e6be4)
   > gas price:           137.5017384 gwei
   > value sent:          0 ETH
   > total cost:          6.041378129628816 ETH

   > Saving artifacts
   -------------------------------------
   > Total cost:     6.041378129628816 ETH

Summary
=======
> Total deployments:   1
> Final cost:          6.041378129628816 ETH

```

This project contains only one migration script which performs two actions: 
   1. Deploying test ERC20 smart-contract
   2. Minting 1 TERC20 token
to **account #1** specified in **truffle-config.js** file on line 11

In migration command output, in the line ```contract address:    0x7364DA3a4989898Ac2d466611Ce4b957885DF7B8``` is our 
new ERC20 token contract address. You can easily import it into your Metamask wallet. After it you can transfer new 
token from previously created **account #1**

## ...Try it with your own contract and have fun!
