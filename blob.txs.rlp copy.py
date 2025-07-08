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
    # tx_rlp_hex = "0xf86c808504e3b2920082524c94c390cc49a32736a58733cf46be42f734dd4f53cb880de0b6b3a76400000125a05ab2f48bdc6752191440ce62088b9e42f20215ee4305403579aa2e1eba615ce8a03b172e53874422756d48b449438407e5478c985680d4aaa39d762fe0d1a11683"
    # # tx_rlp_bytes = bytes.fromhex(tx_rlp_hex[2:])

    # txs = rlp.decode(hex_to_bytes(tx_rlp_hex), Transaction)
    # txs_dict = txs.to_dict()
    
    # # pretty print
    # for key, value in txs_dict.items():
    #     print(f"{key}:\t{value}")

    # encoded = rlp.encode(txs, Transaction)
    # print(f"0x{encoded.hex()}" == tx_rlp_hex)

    # print(txs)

    # tx = decode(tx_rlp_bytes)

    # print(tx)

    # k = keccak.new(digest_bits=256)
    # k.update(tx_rlp_bytes)
    # print(k.hexdigest())

    # data = [
    #     b"",
    #     b"\x04\xe3\xb2\x92\x00",
    #     b"RL",
    #     b"\xc3\x90\xccI\xa3'6\xa5\x873\xcfF\xbeB\xf74\xddOS\xcb",
    #     b"\r\xe0\xb6\xb3\xa7d\x00\x00",
    #     b"\x01",
    #     b"%",
    #     b"Z\xb2\xf4\x8b\xdcgR\x19\x14@\xceb\x08\x8b\x9eB\xf2\x02\x15\xeeC\x05@5y\xaa.\x1e\xbaa\\\xe8",
    #     b';\x17.S\x87D"umH\xb4IC\x84\x07\xe5G\x8c\x98V\x80\xd4\xaa\xa3\x9dv/\xe0\xd1\xa1\x16\x83',
    # ]

    # for d in data:
    #     print(d.hex())

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
