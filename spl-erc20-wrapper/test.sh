#!/bin/bash

if [ -z RECEIVER_PRIVATE_KEY ]; then
  echo "set environment variable RECEIVER_PRIVATE_KEY"
fi

python3 ./deposit_token.py 3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ ./sender.json $RECEIVER_PRIVATE_KEY 0x5EE2CDe31b5d88A0574DAD2B4bb6A073A5b228a8

