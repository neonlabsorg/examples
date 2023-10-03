# Example Subgraph

An example to help you get started with The Graph. For more information see the docs on https://thegraph.com/docs/.
This repository will help in understanding implementation of a subgraph on Neon Devnet.

## Prerequisites

To install Graph CLI globally, run this -

```
npm install -g @graphprotocol/graph-cli
```

## Cloning repository

Run command

```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/the-graph-integration** directory

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
PRIVATE_KEY_1=0x...
PRIVATE_KEY_2=0x...
PRIVATE_KEY_3=0x...
```

## Graph node credentials for Neon Devnet

- Graph endpoint: https://ch2-graph.neontest.xyz/
- Graph endpoint for deploying subgraph: https://ch2-graph.neontest.xyz/deploy/
- Endpoint for graphql: https://ch2-graph.neontest.xyz/index-node/graphql
- IPFS Address: https://ch-ipfs.neontest.xyz/

## Steps to follow for deployment:

1. Run the following commands to install the required packages, compile the Gravatar smart contract and deploy the contract on Neon Devnet.

```
npm install
truffle compile
truffle migrate --network neonlabs
```

2. After getting the contract address and block number from the migration step above, replace the “address” and “startBlock” properties in the “subgraph.yaml” file with the corresponding values.

3. For deploying a subgraph on Neon Devnet, run the following commands -

```
graph create neonlabs/test-subgraph-neon --node https://ch2-graph.neontest.xyz/deploy/
graph codegen
graph build
graph deploy neonlabs/test-subgraph-neon --ipfs https://ch-ipfs.neontest.xyz --node https://ch2-graph.neontest.xyz/deploy/ --version-label="v0.0.1"
```

4. Open the HTTP link from the above result - https://ch2-graph.neontest.xyz/subgraphs/name/neonlabs/test-subgraph-neon

5. To query the subgraph, enter a query like this on the left side -

```
query {
 gravatars {
     displayName
     id
     imageUrl
     owner
  }
}
```
