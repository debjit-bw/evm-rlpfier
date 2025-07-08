import os
from eth_abi import abi
from eth_utils import to_hex
from web3 import HTTPProvider, Web3


def tx_w_chainid(n, acct):
    return {
        "type": 3,
        "chainId": n,  # Anvil
        "from": acct.address,
        "to": "0x0000000000000000000000000000000000000000",
        "value": 0,
        "maxFeePerGas": 10**12,
        "maxPriorityFeePerGas": 10**12,
        "maxFeePerBlobGas": to_hex(10**12),
        "nonce": 0,
    }


def send_blob():
    w3 = Web3(Web3.HTTPProvider("https://rpc.chiadochain.net/"))
    private_key = "PVT_KEY"

    text = "hello world"
    encoded_text = abi.encode(["string"], [text])

    print("Text:", encoded_text)

    # Blob data must be comprised of 4096 32-byte field elements
    # So yeah, blobs must be pretty big
    BLOB_DATA = (b"\x00" * 32 * (4096 - len(encoded_text) // 32)) + encoded_text

    acct = w3.eth.account.from_key(private_key)

    tx = tx_w_chainid(10209, acct)
    gas_estimate = w3.eth.estimate_gas(tx_w_chainid(10200, acct))
    tx["gas"] = gas_estimate

    # This will generate the blobs, commitments, and proofs for our blob tx
    signed = acct.sign_transaction(tx, blobs=[BLOB_DATA])
    print("\n\n\n")
    print(signed.raw_transaction.hex())

if __name__ == "__main__":
    send_blob()