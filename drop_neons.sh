#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: drop_neons.sh <eth-address>"
  exit 1
fi

curl --location --request POST 'http://localhost:3333/request_neon' \
--header 'Content-Type: application/json' \
--data-raw '{
	"wallet": "'${1}'",
	"amount": 1000
}'

