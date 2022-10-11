#!/bin/bash

if [ -z "$GRAPH_ACCESS_TOKEN" ]; then
   echo "CONTRACT_DEPLOYER_PRIVATE_KEY is not set"
fi

yarn -i
yarn create-neon
yarn codegen
yarn deploy-neon

