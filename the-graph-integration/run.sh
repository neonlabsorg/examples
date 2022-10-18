#!/bin/bash

if [ -z "$GRAPH_ACCESS_TOKEN" ]; then
   echo "GRAPH_ACCESS_TOKEN is not set"
   exit 1
fi

yarn -i
yarn create-neon
yarn codegen
yarn deploy-neon

