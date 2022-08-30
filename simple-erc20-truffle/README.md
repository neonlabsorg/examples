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
**NOTE: Currently Metamask plugin for Firefox not working with Neon, please use another browser**
- Connect your metamask wallet to Neon Devnet using these settings:
    - Network Name: Neon Devnet
    - New RPC URL: https://devnet.neonevm.org
    - Chain ID: 245022926
    - Currency Symbol (optional): NEON
- Create new account in Metamask
- Airdrop at most 100 NEONs to just created account [from here](https://neonfaucet.org/)
- Copy your Metamask account private key (Account Details >> Export Private Key)
- Insert just copied private key into quotes in line 8 in file **truffle-config.js** - **NOTE** Add **0x** prefix at the beginning

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
