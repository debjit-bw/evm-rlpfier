from rlp import decode, encode, Serializable
from rlp.sedes import binary
from Crypto.Hash import keccak

class Header(Serializable):
    fields = (
        ('parent_hash', binary),
        ('uncles_hash', binary),
        ('coinbase', binary),
        ('state_root', binary),
        ('transactions_root', binary),
        ('receipts_root', binary),
        ('bloom', binary),
        ('difficulty', binary),
        ('number', binary),
        ('gas_limit', binary),
        ('gas_used', binary),
        ('timestamp', binary),
        ('extra_data', binary),
        ('mix_hash', binary),
        ('nonce', binary),
    )

def main():
    data = [
        bytes.fromhex("bb4039fe0bf6b9719897a067a4a2c2c507d6e6a08e17edc32dcb50ddc4ab2445"), # parent
        bytes.fromhex("1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347"), # uncle
        bytes.fromhex("10aae121b3c62f3dafec9cc46c27b4c1dfe4a835"), # coinbase
        bytes.fromhex("e1726ed3056321dfc079aa81feaa4093d4e0b1f2b086a40d6773d10b98cb749f"), # state_root
        bytes.fromhex("56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"), # transactions_root
        bytes.fromhex("56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"), # receipts_root
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # bloom
        bytes.fromhex("fffffffffffffffffffffffffffffffe"), # difficulty
        bytes.fromhex("4c4b48"), # number
        bytes.fromhex("989680"), # gas_limit
        b'', # gas_used
        bytes.fromhex("5d425beb"), # timestamp
        bytes.fromhex("de830204068f5061726974792d457468657265756d86312e33342e31826c69"), # extra_data
        bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000000"), # mix_hash
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
    print(encode(data))

    k = keccak.new(digest_bits=256)
    # k.update(bytes.fromhex('f90213a01e77d8f1267348b516ebc4f4da1e2aa59f85f0cbd853949500ffac8bfc38ba14a01dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347942a65aca4d5fc5b5c859090a6c34d164135398226a00b5e4386680f43c224c5c037efc0b645c8e1c3f6b30da0eec07272b4e6f8cd89a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421b901000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000086057a418a7c3e83061a80832fefd880845622efdc96d583010202844765746885676f312e35856c696e7578a03fbea7af642a4e20cd93a945a1f5e23bd72fc5261153e09102cf718980aeff38886af23caae95692ef'))
    block = data[0]
    # block.append(b'')
    k.update(encode(block))
    print("HASH: ")
    print(k.hexdigest())

    print(
        "\n\n",
        "parent   :\t", data[0][0].hex(), "\n",
        "uncle    :\t", data[0][1].hex(), "\n",
        "coinbase :\t", data[0][2].hex(), "\n",
        "stat root:\t", data[0][3].hex(), "\n",
        "tx root  :\t", data[0][4].hex(), "\n",
        "rcpt root:\t", data[0][5].hex(), "\n",
        "bloom    :\t", data[0][6].hex(), "\n",
        "diff     :\t", int.from_bytes(data[0][7]), "\n",
        "number   :\t", int.from_bytes(data[0][8]), "\n",
        "gas limit:\t", int.from_bytes(data[0][9]), "\n",
        "gas used :\t", int.from_bytes(data[0][10]), "\n",
        "timestamp:\t", int.from_bytes(data[0][11]), "\n",
        "extra    :\t", data[0][12].hex(), "\n",
        "mix hash :\t", data[0][13].hex(), "\n",
        "nonce    :\t", int.from_bytes(data[0][14]), "\n",
        "unknown  :\t", data[1], "\n",
        "unknown  :\t", data[2], "\n",
    )

    sample_header = Header(
        parent_hash=b'\x00' * 32,
        uncles_hash=b'\x00' * 32,
        coinbase=b'\x00' * 20,
        state_root=b'\x00' * 32,
        transactions_root=b'\x00' * 32,
        receipts_root=b'\x00' * 32,
        bloom=b'\x00' * 256,
        difficulty=b'\x00' * 32,
        number=b'\x00',
        gas_limit=b'\x00' * 32,
        gas_used=b'\x00' * 32,
        timestamp=b'\x00',
        extra_data=b'',
        mix_hash=b'\x00' * 32,
        nonce=b'\x00',
    )
    print("---\n---\n---\n")
    encoded = encode([sample_header])
    print("encoded: ", encoded)
    decoded_rlps = decode(encoded)
    print(type(decoded_rlps))
    header1 = decode(encode(decoded_rlps[0]), Header)
    print(header1)
    print(int.from_bytes(b'\x98\x96\x80', 'big'))
    print(b'@\xcfD0\xec\xaas7\x87\xd1\xa6QT\xa3\xb9\xef\xb5`\xc9]\x9e2J#\xb9\x7f\x06\t\xb59\x13;'.hex())

    # in a file write an array of 

if __name__ == '__main__':
    main()