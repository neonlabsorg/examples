from common import *
import os
os.environ['SOLANA_URL'] = str(selected_network['solana'])
os.environ['EVM_LOADER'] = str(selected_network['evm_loader'])
os.environ["NEON_CLI_TIMEOUT"] = "5.0"

from common_neon.deposit_erc20 import TokenGate
from solana.publickey import PublicKey
import sys
import json
from solana.account import Account as SolanaAccount

# USDT
# python3 ./deposit_token.py 3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ ~/.config/solana/id.json 0x42679bb84732ca108204abdd4841a716ba43593cba16a61f3289c0842e2f5e42 0x5EE2CDe31b5d88A0574DAD2B4bb6A073A5b228a8

if __name__ == "__main__":
    token_mint = PublicKey(sys.argv[1])
    sender_id_file = sys.argv[2]
    neon_account = neon_client.eth.account.from_key(NeonPrivateKey(bytes.fromhex(sys.argv[3])))
    wrapper_address = sys.argv[4]

    with open(sender_id_file) as f:
        d = json.load(f)
    solana_account = SolanaAccount(d[0:32])

    token_gate = TokenGate(
        solana_client, 
        neon_client, 
        token_mint, 
        wrapper_address
    )

    token_gate.deposit_erc20(solana_account, neon_account)
