from solana.rpc.api import Client as SolanaClient
from web3 import Web3
from eth_keys.datatypes import PrivateKey as NeonPrivateKey
from os.path import expanduser, join
from solana.account import Account as SolanaAccount
from solana.publickey import PublicKey
import json
import os

# Connectors
solana_client = SolanaClient('https://api.devnet.solana.com')
neon_client = Web3(Web3.HTTPProvider('https://proxy.devnet.neonlabs.org/solana'))

# Accounts
neon_account = neon_client.eth.account.from_key(NeonPrivateKey(bytes.fromhex('42679bb84732ca108204abdd4841a716ba43593cba16a61f3289c0842e2f5e42')))

home = expanduser("~")
with open(join(home, ".config/solana/id.json")) as f:
    d = json.load(f)
solana_account = SolanaAccount(d[0:32])     

TEST_TOKEN_MINT = PublicKey(os.environ['AWESOME_TOKEN_ADDRESS'])
