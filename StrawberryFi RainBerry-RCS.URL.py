#####Readme.md#####

a new code Bulkhead that helps the Earth Manifest Rain In drought spells using the StrawberryFi AiBot



import os
from web3 import Web3

# Securely pull credentials from GitHub Secrets or Environment Variables
RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
TOKEN_ADDRESS = "0xcb76314c2540199f4b844d4ebbc7998c604880ca" # BERRY Token

# ERC-20 Transfer ABI
ABI = '[{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"type":"function"}]'

def make_it_rain(wallet_list, amount_per_wallet):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    account = w3.eth.account.from_key(PRIVATE_KEY)
    contract = w3.eth.contract(address=Web3.to_checksum_address(TOKEN_ADDRESS), abi=ABI)
    
    amount_wei = w3.to_wei(amount_per_wallet, 'ether')
    
    for recipient in wallet_list:
        try:
            nonce = w3.eth.get_transaction_count(account.address)
            tx = contract.functions.transfer(Web3.to_checksum_address(recipient), amount_wei).build_transaction({
                'chainId': 1,
                'gas': 100000,
                'gasPrice': w3.eth.gas_price,
                'nonce': nonce,
            })
            signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
            hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f"Success: {recipient} | Hash: {w3.to_hex(hash)}")
        except Exception as e:
            print(f"Failed for {recipient}: {e}")

if __name__ == "__main__":
    # Add your list of target wallets here
    targets = ["0x123...", "0x456..."]
    make_it_rain(targets, 1.0) 
