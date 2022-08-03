from erc20_wrapper import ERC20Wrapper
from common import *
import sys
from spl.token.instructions import get_associated_token_address


def deposit(token_mint: PublicKey):
    from_spl_token_acc = get_associated_token_address(solana_account.public_key(), token_mint)
    to_neon_acc = self.create_eth_account()

    print(f'        OWNER {solana_account.public_key()}')
    print(f'            SPL TOKEN ACC {from_spl_token_acc}')

    self.assertEqual(self.wrapper.get_balance(from_spl_token_acc), mint_amount)
    self.assertEqual(self.wrapper.get_balance(to_neon_acc.address), 0)

    TRANSFER_AMOUNT = 123456
    trx = TransactionWithComputeBudget()
    trx.add(self.create_account_instruction(to_neon_acc.address, solana_account.public_key()))
    trx.add(SplTokenInstrutions.approve(SplTokenInstrutions.ApproveParams(
            program_id=self.token.program_id,
            source=from_spl_token_acc,
            delegate=self.wrapper.get_neon_account_address(to_neon_acc.address),
            owner=solana_account.public_key(),
            amount=TRANSFER_AMOUNT,
            signers=[],
    )))
    claim_instr = self.wrapper.create_claim_instruction(
            owner = solana_account.public_key(),
            from_acc=from_spl_token_acc, 
            to_acc=to_neon_acc,
            amount=TRANSFER_AMOUNT,
    )
    trx.add(claim_instr.make_noniterative_call_transaction(len(trx.instructions)))

    opts = TxOpts(skip_preflight=True, skip_confirmation=False)
    print(self.solana_client.send_transaction(trx, solana_account, opts=opts))
    

if __name__ == "__main__":
    token_mint = PublicKey(sys.argv[1])
    deposit(token_mint)
