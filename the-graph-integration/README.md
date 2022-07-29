# Example Subgraph

An example to help you get started with The Graph. For more information see the docs on https://thegraph.com/docs/.

# Steps

Install dependencies
> yarn -i

Run local environment
> docker-compose up -d

Drop tokens to deployer
> ./drop_neons.sh

Compile and deploy smart-contracts
> truffle compile
> truffle migrate --network neonlabs

Create subgraph
> yarn create-local

Generate code
> yarn codegen

Deploy subgraph
> yarn deploy-local

Go to http://127.0.0.1:8000/subgraphs/name/neonlabs/example-subgraph to execute some queries
