#!/bin/bash

docker logs proxy > ./proxy.log 2>&1
docker logs graph-node > ./graph-node.log 2>&1
docker logs neon-tracer > ./neon-tracer.log 2>&1
docker logs neon-rpc > ./neon-rpc.log 2>&1

