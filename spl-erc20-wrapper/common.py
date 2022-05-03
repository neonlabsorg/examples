from solana.rpc.api import Client as SolanaClient
from web3 import Web3
from eth_keys.datatypes import PrivateKey as NeonPrivateKey
from os.path import expanduser, join
from solana.account import Account as SolanaAccount
from solana.publickey import PublicKey
import json
import os

networks = {
  'devnet': {
    'solana': 'https://api.devnet.solana.com',
    'proxy': 'https://proxy.devnet.neonlabs.org/solana',
    'evm_loader': PublicKey('eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU'),
    'neon_token': PublicKey('89dre8rZjLNft7HoupGiyxu3MNftR577ZYu8bHe2kK7g')
  }
}

selected_network = networks['devnet']

solana_client = SolanaClient(selected_network['solana'])
neon_client = Web3(Web3.HTTPProvider(selected_network['proxy']))

# Accounts
neon_account = neon_client.eth.account.from_key(NeonPrivateKey(bytes.fromhex('41ac2becab52d55cb204c65366c3475189064d1d612cc2552103b96de0909ec4')))

home = expanduser("~")
with open(join(home, ".config/solana/id.json")) as f:
    d = json.load(f)
solana_account = SolanaAccount(d[0:32])     

TEST_TOKEN_MINT = PublicKey(os.environ['AWESOME_TOKEN_ADDRESS'])
