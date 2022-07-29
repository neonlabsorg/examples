#!/bin/bash

curl --location --request POST 'http://localhost:3333/request_neon' \
--header 'Content-Type: application/json' \
--data-raw '{
	"wallet":"0xf71c4DACa893E5333982e2956C5ED9B648818376",
	"amount": 1000
}'

curl --location --request POST 'http://localhost:3333/request_neon' \
--header 'Content-Type: application/json' \
--data-raw '{
	"wallet":"0x1D4F1FC4a8dFc0eB612f08Ba3e59291F5eD2C153",
	"amount": 1000
}'

curl --location --request POST 'http://localhost:3333/request_neon' \
--header 'Content-Type: application/json' \
--data-raw '{
	"wallet":"0x4A97d583B1Dd9B6Df50583676dB9ec7fE6Ec4FDA",
	"amount": 1000
}'

