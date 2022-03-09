from solana.rpc.api import Client as SolanaClient
from web3 import Web3
from eth_keys.datatypes import PrivateKey as NeonPrivateKey
from os.path import expanduser, join
from solana.account import Account as SolanaAccount
from solana.publickey import PublicKey
import json
import os

# DEVNET
networks = {
  'devnet': {
    'solana': 'https://api.devnet.solana.com',
    'proxy': 'https://proxy.devnet.neonlabs.org/solana',
    'evm_loader': PublicKey('eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU'),
    'neon_token': PublicKey('89dre8rZjLNft7HoupGiyxu3MNftR577ZYu8bHe2kK7g')
  },
  'nightstand': {
    'solana': 'http://proxy.night.stand.neontest.xyz/node-solana',
    'proxy': 'http://proxy.night.stand.neontest.xyz/solana',
    'evm_loader': PublicKey('53DfF883gyixYNXnM7s5xhdeyV8mVk9T4i2hGV9vG9io'),
    'neon_token': PublicKey('HPsV9Deocecw3GeZv1FkAPNCBRfuVyfw9MMwjwRe1xaU')
  }
}

selected_network = networks['nightstand']

print(f"Solana: {selected_network['solana']}")
print(f"Proxy: {selected_network['proxy']}")

solana_client = SolanaClient(selected_network['solana'])
neon_client = Web3(Web3.HTTPProvider(selected_network['proxy']))

# Accounts
neon_account = neon_client.eth.account.from_key(NeonPrivateKey(bytes.fromhex('f5c746b15e3bdd6bf8c516031a15de16ea161ce10552635abb27c9bd16e0a04a')))

home = expanduser("~")
with open(join(home, ".config/solana/id.json")) as f:
    d = json.load(f)
solana_account = SolanaAccount(d[0:32])     

TEST_TOKEN_MINT = PublicKey(os.environ['AWESOME_TOKEN_ADDRESS'])
