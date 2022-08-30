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
accounts to run this example. To do this: 
1. Setup your Metamask wallet to work with Neon devnet:

    - Connect your metamask wallet to Neon Devnet using these settings:
        - Network Name: Neon Devnet
        - New RPC URL: https://devnet.neonevm.org
        - Chain ID: 245022926
        - Currency Symbol (optional): NEON

2. Create 2 new accounts in Metamask
3. Airdrop at most 100 NEONs to just created accounts [from here](https://neonfaucet.org/)
4. Copy your Metamask account's private keys (Account Details >> Export Private Key) and insert them into **truffle-config.js** 
    at lines 11, 12 in place of compromised keys **NOTE** Add **0x** prefix at the beginning

## Running tests on denvet

Execute command

```sh
truffle test --network neonlabs
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
> Everything is up to date, there is nothing to compile.


  Contract: TestERC20
    ✓ should successfully mint 10000 ERC20 in the first account (5308ms)
    ✓ should transfer token correctly (10426ms)


  2 passing (16s)

```

## Compiling and deploying contract

1. Compiling contract
```sh
truffle compile
```
3. Deploying contract
```sh
truffle migrate --network neonlabs
```

## ...Try it with your own contract and have fun!
