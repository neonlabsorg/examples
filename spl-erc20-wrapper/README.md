
 # Prepare
 > pip3 install -r requirements.txt

# Case 1 - transfer to new account

1. Create new Metamask account
2. Import asset 0x5EE2CDe31b5d88A0574DAD2B4bb6A073A5b228a8 (USTD-F)
3. Go to account details -> export private key -> Copy your private key
4. Go to console and run
    > export RECEIVER_PRIVATE_KEY=*your metamask private key*

5. Run in console from this directory
    > ./test.sh

## Expected
    You should get output like:

```
Failed to configure logged_groups package, file not found: log_cfg.json
token.pubkey = 3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ
        OWNER BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
            SPL TOKEN ACC F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
            RECEIVER: 0xd73C738BD034402084e3E15b0975cB5B268993B1

dest_address_solana = BCJQmgsZc1utTkyrhYkET93vcZwYAfF46Rzx3P472ANy
payer = BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
program_id = TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
source = F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
delegate = BCJQmgsZc1utTkyrhYkET93vcZwYAfF46Rzx3P472ANy
owner = BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
amount = 123456
{'jsonrpc': '2.0', 'result': {'blockTime': 1659618389, 'meta': {'err': None, 'fee': 10000, 'innerInstructions': [{'index': 2, 'instructions': [{'accounts': [0, 1], 'data': '111112gQz8Q2DLChCrULekEzng4Dg8jH9eBetS8nP35LPaaZLFxZsgkdHGPGuaPPB7w9cc', 'programIdIndex': 10}]}, {'index': 5, 'instructions': [{'accounts': [0, 3], 'data': '3Bxs4PckVVt51W8w', 'programIdIndex': 10}, {'accounts': [0, 9], 'data': '11119os1e9qSs2u7TsThXqkBSRVFxhmYaFKFZ1waB2X7armDmvK3p5GmLdUxYdg3h7QSrL', 'programIdIndex': 10}, {'accounts': [9, 7, 6], 'data': '5s6H5oVn6SUxvpgprnqNjuq4NwnqYnfp1CKV7W9154g6A', 'programIdIndex': 8}, {'accounts': [2, 9, 1], 'data': '3QK1PgBtAWnb', 'programIdIndex': 8}]}], 'loadedAddresses': {'readonly': [], 'writable': []}, 'logMessages': ['Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU invoke [1]', 'Program log: Instruction: Create Account', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program log: Total memory occupied: 488', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU consumed 8882 of 499944 compute units', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [1]', 'Program log: Instruction: Approve', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 2902 of 491006 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU invoke [1]', 'Program log: Instruction: Execute Transaction from Instruction', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]', 'Program log: Instruction: InitializeAccount2', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4362 of 323655 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]', 'Program log: Instruction: Transfer', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4735 of 316048 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program data: TE9HMw== XuLN4xtdiKBXTa0rS7agc6WyKKg= AwAAAAAAAAA= 3fJSrRviyJtpwrBo/DeNqpUrp/FjxKEWKPVaTfUjs+8= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA= AAAAAAAAAAAAAAAA1zxzi9A0QCCE4+FbCXXLWyaJk7E=  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4kA=', 'Program log: ExitSucceed: Machine encountered an explict return. exit_status=0x12', 'Program data: UkVUVVJO Eg== 9GkfAAAAAAA= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE=', 'Program log: Total memory occupied: 22433', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU consumed 181604 of 488048 compute units', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU success'], 'postBalances': [4994312400, 1559040, 2039280, 9413700880, 1559040, 60997440, 1009200, 1461600, 934087680, 2039280, 1, 1, 0, 1141440, 1], 'postTokenBalances': [{'accountIndex': 2, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '99876544', 'decimals': 6, 'uiAmount': 99.876544, 'uiAmountString': '99.876544'}}, {'accountIndex': 9, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '123456', 'decimals': 6, 'uiAmount': 0.123456, 'uiAmountString': '0.123456'}}], 'preBalances': [4997925720, 0, 2039280, 9413695880, 1559040, 60997440, 1009200, 1461600, 934087680, 0, 1, 1, 0, 1141440, 1], 'preTokenBalances': [{'accountIndex': 2, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '100000000', 'decimals': 6, 'uiAmount': 100.0, 'uiAmountString': '100'}}], 'rewards': [], 'status': {'Ok': None}}, 'slot': 152694423, 'transaction': {'message': {'accountKeys': ['BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'BCJQmgsZc1utTkyrhYkET93vcZwYAfF46Rzx3P472ANy', 'F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt', '95VnNXsHhgj3Je1wAHSUcxHr88fQAi3QSNTt3yJzGUdc', '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'DUJYS7rDSKLaTogSNeeuHemFPTPCRFsGQ7Rw3MVx3SSo', 'SysvarRent111111111111111111111111111111111', '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', '4kkwKdW4KayA68ULyorgqZD7exf1HhUDoQojzKwbbfZp', '11111111111111111111111111111111', 'KeccakSecp256k11111111111111111111111111111', 'Sysvar1nstructions1111111111111111111111111', 'eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU', 'ComputeBudget111111111111111111111111111111'], 'header': {'numReadonlySignedAccounts': 0, 'numReadonlyUnsignedAccounts': 5, 'numRequiredSignatures': 1}, 'instructions': [{'accounts': [], 'data': '16TYTJ8fLSxF', 'programIdIndex': 14}, {'accounts': [], 'data': '7YXqSw', 'programIdIndex': 14}, {'accounts': [0, 10, 1], 'data': '7k3HJTsZmKmwDiaCcPFMCFAb8JPYWq', 'programIdIndex': 13}, {'accounts': [2, 1, 0], 'data': '498XbEqWSBH1', 'programIdIndex': 8}, {'accounts': [11], 'data': '2CgVnE6omdn41GtC', 'programIdIndex': 11}, {'accounts': [12, 0, 3, 1, 10, 13, 1, 4, 5, 6, 7, 8, 9, 2], 'data': '2KAjkYBDpCXwdhNUJfSEw1yKx7MCCrVf1N4xQRZy3k2fgeUzFxAma114ijXRwnhVr3yL7XRpHput41J3uSKyKjo45AcwfaJWSrdxbrnqnLeaogFqWkjRoidU7qsn98sXJcWravemHLMwUsLAmcH99aJqyafA2SkvA8QsSgURhT2iTjMpNz8hjHVdXVRjEPMYf8acSYUiF2kHwJw7uMAbD2vvWosGHj5LvJAxLV6MT2qRvKoRoCDEoMTu46tSAzJ3YcxeTTFUoobQK', 'programIdIndex': 13}], 'recentBlockhash': '2pPAbbu3yuwZZqTVkeCjYhQ5kGQAk8UZBvexAMLgm4qo'}, 'signatures': ['4MBDh9pXQrvXnd43JbthWeMwTTYa8dmQ227oSnUSyN6bq2mqRvEXf3wDLT3xXFA15LD9YuMtvUz6YoqwNpNm3HL4']}}, 'id': 5}
```

Go to the end of output. There you can find transaction signature:
```
'signatures': ['4MBDh9pXQrvXnd43JbthWeMwTTYa8dmQ227oSnUSyN6bq2mqRvEXf3wDLT3xXFA15LD9YuMtvUz6YoqwNpNm3HL4']
```
Go to solscan to view transaction details

https://solscan.io/tx/4MBDh9pXQrvXnd43JbthWeMwTTYa8dmQ227oSnUSyN6bq2mqRvEXf3wDLT3xXFA15LD9YuMtvUz6YoqwNpNm3HL4?cluster=devnet



Transaction should finalized successfully

Your metamask balance of USDTs should be 0.12345

# Case 2 - transfer to exising account with no USDT balance

1. Create new metamask account
2. Drop some NEONs to this new account from https://neonfaucet.org
3. Import asset 0x5EE2CDe31b5d88A0574DAD2B4bb6A073A5b228a8 (USTD-F)
4. Go to account details -> export private key -> Copy your private key
5. Go to console and run
   > export RECEIVER_PRIVATE_KEY=*your metamask private key*

6. Run in console from this directory
   > ./test.sh

## Expected

    You should get output likeL:

```
Failed to configure logged_groups package, file not found: log_cfg.json
token.pubkey = 3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ
        OWNER BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
            SPL TOKEN ACC F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
            RECEIVER: 0xffb0fb6F4595FEEB3C93153597c541849F8d2DB3

program_id = TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
source = F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
delegate = 8r7dETf6KAZvvzbTqyZGpJY8aFDNrfKvBW5eMt3Aq4WV
owner = BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
amount = 123456
{'jsonrpc': '2.0', 'result': {'blockTime': 1659620150, 'meta': {'err': None, 'fee': 10000, 'innerInstructions': [{'index': 4, 'instructions': [{'accounts': [0, 2], 'data': '3Bxs4PckVVt51W8w', 'programIdIndex': 12}, {'accounts': [0, 8], 'data': '11119os1e9qSs2u7TsThXqkBSRVFxhmYaFKFZ1waB2X7armDmvK3p5GmLdUxYdg3h7QSrL', 'programIdIndex': 12}, {'accounts': [8, 9, 7], 'data': '5s6H5oVn6SUxvpgprnqNjuq4NwnqYnfp1CKV7W9154g6A', 'programIdIndex': 6}, {'accounts': [1, 8, 3], 'data': '3QK1PgBtAWnb', 'programIdIndex': 6}]}], 'loadedAddresses': {'readonly': [], 'writable': []}, 'logMessages': ['Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [1]', 'Program log: Instruction: Approve', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 2902 of 499944 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU invoke [1]', 'Program log: Instruction: Execute Transaction from Instruction', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]', 'Program log: Instruction: InitializeAccount2', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4362 of 335815 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]', 'Program log: Instruction: Transfer', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4735 of 328256 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program data: TE9HMw== XuLN4xtdiKBXTa0rS7agc6WyKKg= AwAAAAAAAAA= 3fJSrRviyJtpwrBo/DeNqpUrp/FjxKEWKPVaTfUjs+8= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA= AAAAAAAAAAAAAAAA/7D7b0WV/us8kxU1l8VBhJ+NLbM=  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4kA=', 'Program log: ExitSucceed: Machine encountered an explict return. exit_status=0x12', 'Program data: UkVUVVJO Eg== 9GkfAAAAAAA= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE=', 'Program log: Total memory occupied: 22433', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU consumed 178334 of 496986 compute units', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU success'], 'postBalances': [4992233120, 2039280, 9413820880, 1559040, 1559040, 60997440, 934087680, 1009200, 2039280, 1461600, 1, 0, 1, 1141440, 1], 'postTokenBalances': [{'accountIndex': 1, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '99629632', 'decimals': 6, 'uiAmount': 99.629632, 'uiAmountString': '99.629632'}}, {'accountIndex': 8, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '123456', 'decimals': 6, 'uiAmount': 0.123456, 'uiAmountString': '0.123456'}}], 'preBalances': [4994287400, 2039280, 9413815880, 1559040, 1559040, 60997440, 934087680, 1009200, 0, 1461600, 1, 0, 1, 1141440, 1], 'preTokenBalances': [{'accountIndex': 1, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '99753088', 'decimals': 6, 'uiAmount': 99.753088, 'uiAmountString': '99.753088'}}], 'rewards': [], 'status': {'Ok': None}}, 'slot': 152699051, 'transaction': {'message': {'accountKeys': ['BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt', '95VnNXsHhgj3Je1wAHSUcxHr88fQAi3QSNTt3yJzGUdc', '8r7dETf6KAZvvzbTqyZGpJY8aFDNrfKvBW5eMt3Aq4WV', '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'DUJYS7rDSKLaTogSNeeuHemFPTPCRFsGQ7Rw3MVx3SSo', 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'SysvarRent111111111111111111111111111111111', '2cJ5XtXkQgNp8piBFBZ1Q7CztmZn6Qw1sLX5jFPtiQnw', '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'KeccakSecp256k11111111111111111111111111111', 'Sysvar1nstructions1111111111111111111111111', '11111111111111111111111111111111', 'eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU', 'ComputeBudget111111111111111111111111111111'], 'header': {'numReadonlySignedAccounts': 0, 'numReadonlyUnsignedAccounts': 5, 'numRequiredSignatures': 1}, 'instructions': [{'accounts': [], 'data': '16TYTJ8fLSxF', 'programIdIndex': 14}, {'accounts': [], 'data': '7YXqSw', 'programIdIndex': 14}, {'accounts': [1, 3, 0], 'data': '498XbEqWSBH1', 'programIdIndex': 6}, {'accounts': [10], 'data': '2CgVmVHHZaFFf7s9', 'programIdIndex': 10}, {'accounts': [11, 0, 2, 3, 12, 13, 4, 5, 3, 6, 7, 8, 9, 1], 'data': '2KAjkYBb18qmgDZLLaBAbc2z3WogwRssw5tCTutSJmjdMrFXkpwkzGATkK2ZDX279eXVHu2JLm2pgdEQbRGS3xYc1vrRjaPFQ4oGg8og1nLQ1cySerAgi3CDrZ5K76HR6g7EWzNsTCHSDv1VZP6nnXVTVszhGo9DzHREHKUXPRG8Zwt7GGjpDKwUB3RSDSgWugcSFJq6bvr9nLhYWwVbARU37PruxiDbCaGWeibLPhc7MBYGkogSZwZyPAiEJA1PLvr598jawyoKu', 'programIdIndex': 13}], 'recentBlockhash': '5NvfcbRti2iPdiGfoUZvWET4zp4sRv6BV9iTfbq2TLgm'}, 'signatures': ['zhxskcb4DQEEMc4K4X2cJLNGVb3Hq98q1TyhcHfpt6Gwvt629uEgbjrSUuYSMC6FL1kLac36uRpn156Xj3vCXTX']}}, 'id': 6}
```

Go to the end of output. There you can find transaction signature:

```
'signatures': ['zhxskcb4DQEEMc4K4X2cJLNGVb3Hq98q1TyhcHfpt6Gwvt629uEgbjrSUuYSMC6FL1kLac36uRpn156Xj3vCXTX']
```

Go to solscan to view transaction details

https://solscan.io/tx/zhxskcb4DQEEMc4K4X2cJLNGVb3Hq98q1TyhcHfpt6Gwvt629uEgbjrSUuYSMC6FL1kLac36uRpn156Xj3vCXTX?cluster=devnet

Transaction should finalized successfully

Your metamask balance of USDTs should be 0.12345

# Case 3 - transfer to existing account with exsisting USDT balance

1. Use metamask account with existing USDT balance (from Case 1 for example)
2. Go to account details -> export private key -> Copy your private key
3. Go to console and run
   > export RECEIVER_PRIVATE_KEY=*your metamask private key*

4. Run in console from this directory
   > ./test.sh

## Expected
    You should get output like:

```
Failed to configure logged_groups package, file not found: log_cfg.json
token.pubkey = 3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ
        OWNER BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
            SPL TOKEN ACC F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
            RECEIVER: 0xd73C738BD034402084e3E15b0975cB5B268993B1

program_id = TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
source = F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt
delegate = BCJQmgsZc1utTkyrhYkET93vcZwYAfF46Rzx3P472ANy
owner = BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe
amount = 123456
{'jsonrpc': '2.0', 'result': {'blockTime': 1659619501, 'meta': {'err': None, 'fee': 10000, 'innerInstructions': [{'index': 4, 'instructions': [{'accounts': [0, 2], 'data': '3Bxs4PckVVt51W8w', 'programIdIndex': 10}, {'accounts': [1, 6, 3], 'data': '3QK1PgBtAWnb', 'programIdIndex': 7}]}], 'loadedAddresses': {'readonly': [], 'writable': []}, 'logMessages': ['Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [1]', 'Program log: Instruction: Approve', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 2902 of 499944 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU invoke [1]', 'Program log: Instruction: Execute Transaction from Instruction', 'Program 11111111111111111111111111111111 invoke [2]', 'Program 11111111111111111111111111111111 success', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]', 'Program log: Instruction: Transfer', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4735 of 361643 compute units', 'Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success', 'Program data: TE9HMw== XuLN4xtdiKBXTa0rS7agc6WyKKg= AwAAAAAAAAA= 3fJSrRviyJtpwrBo/DeNqpUrp/FjxKEWKPVaTfUjs+8= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA= AAAAAAAAAAAAAAAA1zxzi9A0QCCE4+FbCXXLWyaJk7E=  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4kA=', 'Program log: ExitSucceed: Machine encountered an explict return. exit_status=0x12', 'Program data: UkVUVVJO Eg== +EMAAAAAAAA= AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE=', 'Program log: Total memory occupied: 20489', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU consumed 144847 of 496986 compute units', 'Program eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU success'], 'postBalances': [4994287400, 2039280, 9103952880, 1559040, 1559040, 60997440, 2039280, 934087680, 1, 0, 1, 1141440, 1], 'postTokenBalances': [{'accountIndex': 1, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '99753088', 'decimals': 6, 'uiAmount': 99.753088, 'uiAmountString': '99.753088'}}, {'accountIndex': 6, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '246912', 'decimals': 6, 'uiAmount': 0.246912, 'uiAmountString': '0.246912'}}], 'preBalances': [4994302400, 2039280, 9103947880, 1559040, 1559040, 60997440, 2039280, 934087680, 1, 0, 1, 1141440, 1], 'preTokenBalances': [{'accountIndex': 1, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': 'BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '99876544', 'decimals': 6, 'uiAmount': 99.876544, 'uiAmountString': '99.876544'}}, {'accountIndex': 6, 'mint': '3vxj94fSd3jrhaGAwaEKGDPEwn5Yqs81Ay5j1BcdMqSZ', 'owner': '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'uiTokenAmount': {'amount': '123456', 'decimals': 6, 'uiAmount': 0.123456, 'uiAmountString': '0.123456'}}], 'rewards': [], 'status': {'Ok': None}}, 'slot': 152697344, 'transaction': {'message': {'accountKeys': ['BXriNC3FzEMqwc8epFRwy81qeQTzzreNV1konmG28Pe', 'F2BYmd7RNkwbk3AdxnYTMBhTjfgs9LFieyiKTGJpMipt', 'piPJ1veB1JUEygPJDUJNUWsKnTXzYrBoDQj2bQYEGid', 'BCJQmgsZc1utTkyrhYkET93vcZwYAfF46Rzx3P472ANy', '7RD9rskVjjAdhNJBA2XzpJE2wtYNsLgVTWDujQAnoS9k', 'DUJYS7rDSKLaTogSNeeuHemFPTPCRFsGQ7Rw3MVx3SSo', '4kkwKdW4KayA68ULyorgqZD7exf1HhUDoQojzKwbbfZp', 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'KeccakSecp256k11111111111111111111111111111', 'Sysvar1nstructions1111111111111111111111111', '11111111111111111111111111111111', 'eeLSJgWzzxrqKv1UxtRVVH8FX3qCQWUs9QuAjJpETGU', 'ComputeBudget111111111111111111111111111111'], 'header': {'numReadonlySignedAccounts': 0, 'numReadonlyUnsignedAccounts': 5, 'numRequiredSignatures': 1}, 'instructions': [{'accounts': [], 'data': '16TYTJ8fLSxF', 'programIdIndex': 12}, {'accounts': [], 'data': '7YXqSw', 'programIdIndex': 12}, {'accounts': [1, 3, 0], 'data': '498XbEqWSBH1', 'programIdIndex': 7}, {'accounts': [8], 'data': '2CgVmVHHZaFFf7s9', 'programIdIndex': 8}, {'accounts': [9, 0, 2, 3, 10, 11, 3, 4, 5, 1, 6, 7], 'data': '2K7JyEnStvLu8uZDoba3Kh22zF7xEnN98qm4UPnYUjyMdWEGHCZP8RZikEgUVijGMymGSEMputaQ82mkESAq64rkjvUpebApP8g5obRChz8xCL2ygjyGuPY1C5cEAW3ajBKizR9yzismyCc7Y1bziALjJWw7xbHfPYnopddBJEKYtVVU91q6onyuEdpfRSqGqEK4W4guJ89826U47GJfnW56mikEb62EdGakCCAtNgFfK8ftueFokRgJd6zHjco4QVcsTz7WisaBR', 'programIdIndex': 11}], 'recentBlockhash': 'BFHdTEsCzwtmiSPrKHjPkfwVewcyZyB6ejmWHhemfvLw'}, 'signatures': ['17nddcV4LLA8fmYQksiVvtnzYyQruuUUs96QdDW8TcEjcGXdoR6QLAGfxGPfrm9C6drffLeS5aFRch9L8jaLmwN']}}, 'id': 6}

```

Go to the end of output. There you can find transaction signature:
```
'signatures': ['17nddcV4LLA8fmYQksiVvtnzYyQruuUUs96QdDW8TcEjcGXdoR6QLAGfxGPfrm9C6drffLeS5aFRch9L8jaLmwN']
```
Go to solscan to view transaction details

https://solscan.io/tx/17nddcV4LLA8fmYQksiVvtnzYyQruuUUs96QdDW8TcEjcGXdoR6QLAGfxGPfrm9C6drffLeS5aFRch9L8jaLmwN?cluster=devnet

Transaction should finalized successfully

Your metamask balance of USDTs should increase by 0.12345