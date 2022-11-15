# brownie_erc20_tokens
- clone the repo

- add the neon devnet to the brownie networks:
`brownie networks import ./network-config.yaml`

- add your accounts to .env file: 
`export ACC1=0x.........` (sender account)
`export ACC2=0x.........` (recipient account)

- add your faucet url to .env file
`export FAUCET_URL=.........`

- compile the contract source files
`brownie compile`

- deploy the erc contract:
`brownie run scripts/deploy.py`

- run test if needed
`brownie test`
