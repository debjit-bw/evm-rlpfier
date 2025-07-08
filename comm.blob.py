import ckzg
import os
from eth_abi import abi
from eth_utils import to_hex
from web3 import HTTPProvider, Web3
import hashlib

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
        "nonce": 1,
    }

def create_blob_data(text):
    # Encode the text using Ethereum ABI encoding for a string
    encoded_text = abi.encode(["string"], [text])
    
    # Calculate the required padding to make the blob size exactly 131072 bytes or 128 KB
    required_padding = 131072 - (len(encoded_text) % 131072)
    
    # Create the BLOB_DATA with the correct padding
    BLOB_DATA = (b"\x00" * required_padding) + encoded_text

    # save the blob data to a file
    with open("blobs/blob.txt", "w") as file:
        file.write(BLOB_DATA.hex())
    
    return BLOB_DATA

def bytes_from_hex(hexstring):
    return bytes.fromhex(hexstring.replace("0x", ""))

def get_commitment():
    ts = ckzg.load_trusted_setup("trusted_setup.txt", 0)
    
    with open("blobs/blob.txt", "r") as file:
        blob_hex = file.read().strip()
        blob = bytes_from_hex(blob_hex)
    
    # Compute KZG commitment
    commitment = ckzg.blob_to_kzg_commitment(blob, ts)
    
    # Print the commitment in hexadecimal format
    print("KZG Commitment:", commitment.hex())

    # commitment = commitment.hex()
    # commitment = commitment[:-1] + "c"
    # commitment = bytes_from_hex(commitment)
    # print(commitment[-1], type(commitment[-1]))

    return commitment

def get_versioned_hash():
    kzg_commitment_bytes = get_commitment()

    # Remove the '0x' prefix if present
    # if kzg_commitment.startswith("0x"):
    #     kzg_commitment = kzg_commitment[2:]

    # Convert the KZG commitment to bytes
    # kzg_commitment_bytes = bytes.fromhex(kzg_commitment)

    # Compute the SHA-256 hash of the KZG commitment
    sha256_hash = hashlib.sha256(kzg_commitment_bytes).digest()

    # Prepend the version byte (0x01) to the last 31 bytes of the SHA-256 hash
    version_byte = b'\x01'
    blob_versioned_hash = version_byte + sha256_hash[1:]

    # Convert to hexadecimal for display
    blob_versioned_hash_hex = blob_versioned_hash.hex()

    # Print the result
    print(f"Blob versioned hash: 0x{blob_versioned_hash_hex}")

    return blob_versioned_hash_hex

def send_blob():
    w3 = Web3(Web3.HTTPProvider("https://rpc.chiadochain.net/"))
    private_key = "PVT_KEY"

    text = "hello world"
    BLOB_DATA = create_blob_data(text)

    acct = w3.eth.account.from_key(private_key)

    tx = tx_w_chainid(10209, acct)
    gas_estimate = w3.eth.estimate_gas(tx_w_chainid(10200, acct))
    tx["gas"] = gas_estimate

    # This will generate the blobs, commitments, and proofs for our blob tx
    signed = acct.sign_transaction(tx, blobs=[BLOB_DATA])
    print("\n\n\n")
    with open("blobs/signed_blob.txt", "w") as file:
        file.write(signed.raw_transaction.hex())

    versioned_hash = get_versioned_hash()
    with open("blobs/versioned_hash.txt", "w") as file:
        file.write(versioned_hash)

if __name__ == "__main__":
    send_blob()