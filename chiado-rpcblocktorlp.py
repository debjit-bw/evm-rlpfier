from rlp import decode, encode
from web3 import Web3
from Crypto.Hash import keccak

def pretty_printer(data_encoded):
    header = decode(data_encoded)
    # print(header)
    print(
        "\n\n",
        "parent   :\t", header[0].hex(), "\n",
        "uncle    :\t", header[1].hex(), "\n",
        "coinbase :\t", header[2].hex(), "\n",
        "stat root:\t", header[3].hex(), "\n",
        "tx root  :\t", header[4].hex(), "\n",
        "rcpt root:\t", header[5].hex(), "\n",
        "bloom    :\t", header[6].hex(), "\n",
        "diff     :\t", header[7].hex(), "\n",
        "number   :\t", header[8].hex(), "\n",
        "gas limit:\t", header[9].hex(), "\n",
        "gas used :\t", header[10].hex(), "\n",
        "timestamp:\t", header[11].hex(), "\n",
        "extra    :\t", header[12].hex(), "\n",
        "mix hash :\t", header[13].hex(), "\n",
        "nonce    :\t", header[14].hex(), "\n",
        "base fee :\t", header[15].hex(), "\n",
    )

block_header = {
    "parentHash": "0x004741e530aa411fff7db274d9a1831c85e5e29b2e681aaec050ab4d0007cbb9",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "miner": "0x88dfc82cf71fdeb23f82c33a202f6e2d19ac0541",
    "stateRoot": "0x69d9ad5fda1ed442fdd85333adbe344a42e82e47942f54d75285d69758c99bba",
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "difficulty": "0x",
    "number": "0xf4240",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x",
    "timestamp": "0x637db0aa",
    "extraData": "0x4e65746865726d696e64",
    "mixHash": "0xc1061c73ce9f60906398fdc51b1e3d4c186aa9d3df2f8f28f15ccdb3f7a04f2b",
    "nonce": "0x0000000000000000",
    "baseFeePerGas": "0x7",
}

# parse hex string to int
block_number = int(block_header["number"], 16)
print(f"Block number: {block_number}")

def convert_to_rlp(block_header = block_header):
    # # print(Web3.to_hex(block_header["gasLimit"]))
    # # print(Web3.to_hex(block_header["gasUsed"]))
    # # print(Web3.to_hex(block_header["timestamp"]))
    # # print(Web3.to_hex(block_header["difficulty"]))
    # # print(Web3.to_hex(block_header["number"]))

    # print(Web3.to_hex(bytes.fromhex("1c9c380")))
    store = []
    for key, value in block_header.items():
        # print(f"> {key}")
        # if key in ["difficulty", "number", "gasLimit", "gasUsed", "timestamp"]:
        #     print(f"HEX: {value} -> {Web3.to_bytes(hexstr=value)}")
        store.append(Web3.to_bytes(hexstr=value))
        # else:
        #     store.append(bytes.fromhex(value[2:]))
        # print(">> ", store[-1].hex())

    # write rlp to file
    with open(f"chiado-block_{block_number}_selfencoded.rlp", "wb") as f:
        f.write(encode(store))

    rlp_encoded = encode(store)
    # print(rlp_encoded)
    
    pretty_printer(rlp_encoded)

    k = keccak.new(digest_bits=256)
    k.update(rlp_encoded)
    print("HASH: 0x", k.hexdigest())


if __name__ == "__main__":
    convert_to_rlp()