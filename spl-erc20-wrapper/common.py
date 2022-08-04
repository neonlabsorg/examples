from solana.rpc.api import Client as SolanaClient
from common_neon.web3 import NeonWeb3
from web3 import HTTPProvider
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
neon_client = NeonWeb3(HTTPProvider(selected_network['proxy']))   
