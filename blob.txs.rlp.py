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

from eth_utils import to_hex
from eth_abi import abi

# "https://rpc.chiadochain.net/"
w3 = Web3(Web3.HTTPProvider("https://rpc.chiadochain.net/"))

PVT_KEY = "<PRIVATE KEY HERE>"
acc = w3.eth.account.from_key(PVT_KEY)
print(type(acc.address))
print(acc.address)

def pprint(data):
    for key, value in data.items():
        print(f"{key}:\t{value}")

def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


def main():
    text = "Hello World!"
    encoded_text = abi.encode(["string"], [text])

    # Calculate the required padding to make the blob size exactly 131072 bytes
    required_padding = 131072 - (len(encoded_text) % 131072)

    # Create the BLOB_DATA with the correct padding
    BLOB_DATA = (b"\x00" * required_padding) + encoded_text

    transaction = {
        'type': 3,
        'from': acc.address,
        'to': "0x0000000000000000000000000000000000000000",
        'value': 0,
        'nonce': 0,
        'gas': 200000,
        'maxFeePerGas': 10**12,
        'maxPriorityFeePerGas': 10**12,
        'maxFeePerBlobGas': to_hex(1000000000),
        'chainId': 10209,
        # 'blobVersionedHashes': "0x
    }
    pprint(transaction)

    signed_txn = w3.eth.account.sign_transaction(transaction, PVT_KEY, [BLOB_DATA])
    print(signed_txn.raw_transaction.hex())
    # print(rlp.decode(signed_txn.raw_transaction))

if __name__ == "__main__":
    main()
