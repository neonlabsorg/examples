# Example Subgraph

An example to help you get started with The Graph. For more information see the docs on https://thegraph.com/docs/.

# Running on Neon devnet
Install dependencies
> yarn -i

Compile and deploy smart-contracts
> truffle compile
> 
> truffle migrate --network neonlabs

Create subgraph
> yarn create-neon

Generate code
> yarn codegen

Build graph
> yarn build

Deploy subgraph
> yarn deploy-neon

Go to https://ch2-graph.neontest.xyz/subgraphs/name/neonlabs/example-subgraph to execute some queries

# Running on local environment

Install dependencies
> yarn -i

Run local environment
> docker-compose up -d

Drop tokens to deployer
> ./drop_neons.sh

Compile and deploy smart-contracts
> truffle compile
> 
> truffle migrate --network neonlabs

Create subgraph
> yarn create-local

Generate code
> yarn codegen

Deploy subgraph
> yarn deploy-local

Go to http://127.0.0.1:8000/subgraphs/name/neonlabs/example-subgraph to execute some queries
