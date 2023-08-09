# Example deploying ERC20 to Neonlabs devnet using Foundry

This directory contains all the files necessary to deploy simplest ERC20-like contract using Neon onto the Solana blockchain.

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
git clone https://github.com/sukanyaparashar/simple-erc20-foundry.git
```

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
[⠒] Compiling 24 files with 0.8.21
[⠃] Solc 0.8.21 finished in 2.48s
Compiler run successful!
```

2. Running tests

```sh
forge test
```

This command runs the test file ./test/MyToken.t.sol. After successfully running this step you should get console output similar to:

```sh
[⠔] Compiling...
No files changed, compilation skipped

Running 28 tests for test/MyToken.t.sol:ContractTest
[PASS] testApprove() (gas: 33645)
[PASS] testBurn() (gas: 60834)
[PASS] testDescreaseAllowance() (gas: 38912)
[PASS] testFailApproveFromZeroAddress() (gas: 10699)
[PASS] testFailApproveToZeroAddress() (gas: 5707)
[PASS] testFailBurnFromZero() (gas: 5857)
[PASS] testFailBurnInsufficientBalance() (gas: 60529)
[PASS] testFailFuzzBurnInsufficientBalance(address,uint256,uint256) (runs: 256, μ: 53877, ~: 57779)
[PASS] testFailFuzzTransferFromInsufficientApprove(address,address,uint256,uint256) (runs: 256, μ: 82243, ~: 85777)
[PASS] testFailFuzzTransferFromInsufficientBalance(address,address,uint256,uint256) (runs: 256, μ: 79311, ~: 86113)
[PASS] testFailMintToZero() (gas: 5829)
[PASS] testFailTransferFromInsufficientApprove() (gas: 87997)
[PASS] testFailTransferFromInsufficientBalance() (gas: 88354)
[PASS] testFailTransferFromZeroAddress() (gas: 64907)
[PASS] testFailTransferInsufficientBalance() (gas: 62464)
[PASS] testFailTransferInsufficientBalance(address,uint256,uint256) (runs: 256, μ: 54141, ~: 57389)
[PASS] testFailTransferToZeroAddress() (gas: 60182)
[PASS] testFuzzApprove(address,uint256) (runs: 256, μ: 33648, ~: 34504)
[PASS] testFuzzBurn(address,uint256,uint256) (runs: 256, μ: 62230, ~: 64561)
[PASS] testFuzzMint(address,uint256) (runs: 256, μ: 54746, ~: 56923)
[PASS] testFuzzTransfer(address,uint256) (runs: 256, μ: 62238, ~: 63327)
[PASS] testFuzzTransferFrom(address,address,uint256,uint256) (runs: 256, μ: 92481, ~: 98242)
[PASS] testIncreaseAllowance() (gas: 35569)
[PASS] testMint() (gas: 56016)
[PASS] testName() (gas: 9585)
[PASS] testSymbol() (gas: 9608)
[PASS] testTransfer() (gas: 89644)
[PASS] testTransferFrom() (gas: 118902)
Test result: ok. 28 passed; 0 failed; 0 skipped; finished in 36.82ms
Ran 1 test suites: 28 tests passed, 0 failed, 0 skipped (28 total tests)
```

## Deploying contract

```sh
forge create --rpc-url $RPC_URL --private-key $PRIVATE_KEY src/MyToken.sol:MyToken --constructor-args "Test ERC20 Token" "TERC20" --legacy
```

After successfully running this step you should get console output similar to:

```sh
[⠰] Compiling...
No files changed, compilation skipped
Deployer: 0x4455E84Eaa56a01676365D4f86348B311969a4f4
Deployed to: 0x93332B8455CB0a364811c2953896b572804e0629
Transaction hash: 0x084e7ee5cde41d31be6ce4bb0bc4d727a103e287b4ad53e1a6bee69e194325f5
```

## Send a transaction with a deployed smart contract function

```sh
cast send <contract_address> --rpc-url $RPC_URL --private-key $PRIVATE_KEY "mint(address,uint256)" <deployer_address> 20000000000000000000 --legacy
```

After successfully running this step you should get console output similar to:

```sh
blockHash               0x1c50efc0068993375b409344ad426d9224d0fd9c81acbaf77ecab227fc264923
blockNumber             235310270
contractAddress
cumulativeGasUsed       1527280
effectiveGasPrice
gasUsed                 1527280
logs                    [{"address":"0x93332b8455cb0a364811c2953896b572804e0629","topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x0000000000000000000000000000000000000000000000000000000000000000","0x0000000000000000000000004455e84eaa56a01676365d4f86348b311969a4f4"],"data":"0x000000000000000000000000000000000000000000000001158e460913d00000","blockHash":"0x1c50efc0068993375b409344ad426d9224d0fd9c81acbaf77ecab227fc264923","blockNumber":"0xe068cbe","transactionHash":"0x3e692b5b92ee8aefa7a5619bc7241f41926818275dda0323884a5daf5ec35ab8","transactionIndex":"0x0","logIndex":"0x0","transactionLogIndex":"0x0","removed":false}]
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root
status                  1
transactionHash         0x3e692b5b92ee8aefa7a5619bc7241f41926818275dda0323884a5daf5ec35ab8
transactionIndex        0
type                    0
```

## Call a deployed smart contract function

```sh
cast call <contract_address> --rpc-url $RPC_URL "balanceOf(address)" <account_address>
```

After successfully running this step you should get console output similar to:

```sh
0x000000000000000000000000000000000000000000000001158e460913d00000
```

**Note** The returned value is in hexadecimal form. So you can use this [link](https://www.rapidtables.com/convert/number/hex-to-decimal.html) to convert it into decimal form and check the value.

## ...Try it with your own contract and have fun!
