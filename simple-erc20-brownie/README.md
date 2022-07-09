# brownie_neon_token
- clone the repo
- create a .env file, for now empty...
- add the neon devnet to the brownie networks:
`brownie networks import ./network-config.yaml`

- add your account: `brownie accounts new neon_dev` (neon_dev is just a name example)

- deploy the erc contract:
`brownie run scripts/deploy.js --network neon-devnet`
