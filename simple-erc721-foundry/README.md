# Example deploying ERC721 to Neon Labs Devnet using Foundry

This directory contains all the files necessary to deploy simplest ERC721-like contract using Neon onto the Solana blockchain.

## Prerequisites

To use this project, Rust and Foundry must be installed on the machine.

### Rust installation

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Foundry installation

```sh
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

## Cloning repository

Run command

```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/simple-erc721-foundry** directory

## Setup Neon account (using Metamask)

To create new account:

1. Setup your Metamask wallet to work with Neon devnet:

   - Connect your metamask wallet to Neon Devnet using these settings:
     - Network Name: Neon Devnet
     - New RPC URL: https://devnet.neonevm.org
     - Chain ID: 245022926
     - Currency Symbol (optional): NEON

2. Create a new account in Metamask
3. Airdrop at most 100 NEONs to just created **account #1** [from here](https://neonfaucet.org/)
4. Copy your Metamask account's private key (Account Details >> Export Private Key) and insert them into **.env**
   **NOTE!** Add **0x** prefix at the beginning

## Set up .env file

Create a .env file in the root project folder and add these lines -

```sh
RPC_URL=https://devnet.neonevm.org
PRIVATE_KEY=<YOUR_PRIVATE_KEY>
```

Then run this -

```sh
source .env
```

## Building contracts and running tests on devnet

1. Compiling contract

```sh
forge build
```

This command will compile all the contracts. After successfully running this step you should get console output similar to:

```sh
[⠢] Compiling...
[⠒] Compiling 37 files with 0.8.21
[⠃] Solc 0.8.21 finished in 2.44s
Compiler run successful!
```

2. Running tests

```sh
forge test
```

This command runs the test file ./test/MyToken.t.sol. After successfully running this step you should get console output similar to:

```sh
[⠰] Compiling...
No files changed, compilation skipped

Running 3 tests for test/MyFirstNFT.t.sol:MyFirstNFTTest
[PASS] testMint() (gas: 199649)
[PASS] testName() (gas: 9647)
[PASS] testSymbol() (gas: 9691)
Test result: ok. 3 passed; 0 failed; 0 skipped; finished in 565.96µs
Ran 1 test suites: 3 tests passed, 0 failed, 0 skipped (3 total tests)
```

## Deploying contract

```sh
forge create --rpc-url $RPC_URL --private-key $PRIVATE_KEY src/MyFirstNFT.sol:MyFirstNFT --legacy
```

After successfully running this step you should get console output similar to:

```sh
[⠰] Compiling...
No files changed, compilation skipped
Deployer: 0x4455E84Eaa56a01676365D4f86348B311969a4f4
Deployed to: 0xa2eBcA19dcADFd1ab3D387335Eb2BBd337A0Ae2D
Transaction hash: 0x3c81a82ae5a1ae099c1828d21fc10554ae1dc3886bfedeea4df92e09e28b4175
```

## Mint an ERC721 token

```sh
cast send <contract_address> --rpc-url $RPC_URL --private-key $PRIVATE_KEY "safeMint(address,string)" <deployer_address> <token_metadata_uri> --legacy
```

After successfully running this step you should get console output similar to:

```sh
blockHash               0xd271485b917f00b838b7cce0654b18627e66f2afdcacfd9d242589e611cf06bc
blockNumber             237126783
contractAddress
cumulativeGasUsed       6768160
effectiveGasPrice
gasUsed                 6768160
logs                    [{"address":"0xa2ebca19dcadfd1ab3d387335eb2bbd337a0ae2d","topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x0000000000000000000000000000000000000000000000000000000000000000","0x0000000000000000000000004455e84eaa56a01676365d4f86348b311969a4f4","0x0000000000000000000000000000000000000000000000000000000000000000"],"data":"0x","blockHash":"0xd271485b917f00b838b7cce0654b18627e66f2afdcacfd9d242589e611cf06bc","blockNumber":"0xe22447f","transactionHash":"0x29404df19648905b9a8e3153df28977b9ad48f4a261418bcd4b23613559a32dc","transactionIndex":"0x0","logIndex":"0x0","transactionLogIndex":"0x0","removed":false},{"address":"0xa2ebca19dcadfd1ab3d387335eb2bbd337a0ae2d","topics":["0xf8e1a15aba9398e019f0b49df1a4fde98ee17ae345cb5f6b5e2c27f5033e8ce7"],"data":"0x0000000000000000000000000000000000000000000000000000000000000000","blockHash":"0xd271485b917f00b838b7cce0654b18627e66f2afdcacfd9d242589e611cf06bc","blockNumber":"0xe22447f","transactionHash":"0x29404df19648905b9a8e3153df28977b9ad48f4a261418bcd4b23613559a32dc","transactionIndex":"0x0","logIndex":"0x1","transactionLogIndex":"0x1","removed":false}]
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root
status                  1
transactionHash         0x29404df19648905b9a8e3153df28977b9ad48f4a261418bcd4b23613559a32dc
transactionIndex        0
type                    0
```

## Call a deployed smart contract function to get the Token URI

```sh
cast call <contract_address> --rpc-url $RPC_URL "tokenURI(uint256) (string)" 0
```

After successfully running this step you should get console output displaying the token URI similar to this:

```sh
https://......
```

## ...Try it with your own contract and have fun!
