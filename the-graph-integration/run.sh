#!/bin/bash

if [ -z "$GRAPH_ACCESS_TOKEN" ]; then
   echo "GRAPH_ACCESS_TOKEN is not set"
fi

yarn -i
yarn create-neon
yarn codegen
yarn deploy-neon

