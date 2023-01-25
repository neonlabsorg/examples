# Example deploying ERC20 for SPL contract to Neonlabs devnet using Truffle

## Cloning repository
Run command
```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/simple-erc20-spl-truffle** directory

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
3. Run tests from ./test/test_erc20_for_spl.js

After successfully running this step you should get console output similar to:
```sh
Using network 'neonlabs'.


Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.
⠴ Fetching solc version list from solc-bin. Attempt #1

  Contract: ERC20ForSplMintableom solc-bin. Attempt #1
    ✔ should mint 10000 ERC20 (4806ms)-bin. Attempt #1
    ✔ should check name (345ms)om solc-bin. Attempt #1
    ✔ should check symbol (124ms) solc-bin. Attempt #1
    ✔ should check decimals (118ms)olc-bin. Attempt #1
    ✔ should check total supply (5285ms)in. Attempt #1
    ✔ should burn 100 ERC20 (10531ms)c-bin. Attempt #1
    ✔ should transfer token correctly (23639ms)empt #1


  7 passing (1m)

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
> Everything is up to date, there is nothing to compile.
⠦ Fetching solc version list from solc-bin. Attempt #1
⠏ Fetching solc version list from solc-bin. Attempt #1
Starting migrations...
======================
> Network name:    'neonlabs'
> Network id:      245022926
> Block gas limit: 260057650590124 (0xec8563e271ac)


1_erc20_spl.js
==============
⠇ Fetching solc version list from solc-bin. Attempt #1
   Replacing 'ERC20ForSplMintable'
   -------------------------------
   > transaction hash:    0xe90aa063e5e0b0c0af34e15df51402cc7c7a094cad6583038cdf85544fe322bb
   > Blocks: 10           Seconds: 4lc-bin. Attempt #1
   > contract address:    0x5bb40F4685a2a0C7BFA6D9471bC7d2ecF12f9495
   > block number:        191185622
   > block timestamp:     1674603234
   > account:             0x1823085af38c56f080922f19d8E34e87e70DD63c
   > balance:             83.9407635943220638
   > gas used:            120330760 (0x72c1a08)
   > gas price:           101.6042163 gwei
   > value sent:          0 ETH
   > total cost:          12.226112566583388 ETH

   > Saving artifacts
   -------------------------------------
   > Total cost:     12.226112566583388 ETH

Summary
=======
> Total deployments:   1
> Final cost:          12.226112566583388 ETH

```

This project contains only one migration script which performs two actions: 
   1. Deploying test ERC20ForSplMintable smart-contract
to **account #1** specified in **truffle-config.js** file on line 11

In migration command output, in the line ```contract address:    0x5bb40F4685a2a0C7BFA6D9471bC7d2ecF12f9495``` is our 
new ERC20 for Spl token contract address. You can easily import it into your Metamask wallet. After it you can transfer new 
token from previously created **account #1**

## ...Try it with your own contract and have fun!
