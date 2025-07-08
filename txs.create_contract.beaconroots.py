from rlp import decode, encode, Serializable
from rlp.sedes import binary
from Cryptodome.Hash import keccak
from web3 import Web3
from hexbytes import HexBytes

import rlp
from eth_typing import HexStr
from eth_utils import to_bytes
from ethereum.transactions import Transaction
from web3.middleware import SignAndSendRawMiddlewareBuilder

# "https://rpc.chiadochain.net/"
w3 = Web3(Web3.HTTPProvider("https://rpc.chiadochain.net/"))

PVT_KEY = "PVT_KEY"
acc = w3.eth.account.from_key(PVT_KEY)
print(type(acc.address))
print(acc.address)

def pprint(data):
    for key, value in data.items():
        print(f"{key}:\t{value}")

def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


def main():
    deposit_contract_bytecode = bytes.fromhex("60618060095f395ff33373fffffffffffffffffffffffffffffffffffffffe14604d57602036146024575f5ffd5b5f35801560495762001fff810690815414603c575f5ffd5b62001fff01545f5260205ff35b5f5ffd5b62001fff42064281555f359062001fff015500")

    transaction = {
        'from': acc.address,
        # 'to': None,
        'value': 0,
        'nonce': 0,
        'gas': 3836885,
        'gasPrice': 2000000000,
        'data': deposit_contract_bytecode,
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, PVT_KEY)
    print("\n\n\n")
    print(signed_txn.raw_transaction.hex())

if __name__ == "__main__":
    main()
