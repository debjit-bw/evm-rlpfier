from rlp import decode, encode, Serializable
from rlp.sedes import binary
from Cryptodome.Hash import keccak

def print_rec(data, level = 1):
    for d in data:
        try:
            print(f"{'>' * level}\t", d.hex())
        except:
            print(f"arr @ lvl {level}")
            try:
                # print(f"{'[>]' * level}\t", [d_.hex() for d_ in d])
                [print_rec(d_) for d_ in d]
            except:
                print(f"{'!' * level}\t")
                print(d)

def main():
    data = bytes.fromhex("0x03f8968227e18085e8d4a5100085e8d4a510008252089400000000000000000000000000000000000000008080c085e8d4a51000e1a001af254f4973a787397a71597d9492c0d7e52c3d80b42dd51f7ae249954c57bd01a0cf5dee0e4f985aa7921bf5d885868e9345a348536ff43236896cbdd0be5dfcaaa0220ac30b37b2f75ad9b7983478c77e10a8e0891d9403f928688e45fd3a6ac868")
    print(len(data))
    data = decode(data)

    for d in data:
        print_rec(d)
        # try:
        #     print(">\t", d.hex())
        # except:
        #     print("arr:")
        #     try:
        #         print(">>\t", [d_.hex() for d_ in d])
        #     except:
        #         print(d)

    k = keccak.new(digest_bits=256)
    # k.update(bytes.fromhex('f90213a01e77d8f1267348b516ebc4f4da1e2aa59f85f0cbd853949500ffac8bfc38ba14a01dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347942a65aca4d5fc5b5c859090a6c34d164135398226a00b5e4386680f43c224c5c037efc0b645c8e1c3f6b30da0eec07272b4e6f8cd89a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421b901000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000086057a418a7c3e83061a80832fefd880845622efdc96d583010202844765746885676f312e35856c696e7578a03fbea7af642a4e20cd93a945a1f5e23bd72fc5261153e09102cf718980aeff38886af23caae95692ef'))
    block = data[0]
    # block[6] = bytes.fromhex("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    # block[7] = int(0x20000)
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
        "sign     :\t", int.from_bytes(data[0][14]), "\n",
        "unknown  :\t", data[1], "\n",
        "unknown  :\t", data[2], "\n",
    )

    # sample_header = Header(
    #     parent_hash=b'\x00' * 32,
    #     uncles_hash=b'\x00' * 32,
    #     coinbase=b'\x00' * 20,
    #     state_root=b'\x00' * 32,
    #     transactions_root=b'\x00' * 32,
    #     receipts_root=b'\x00' * 32,
    #     bloom=b'\x00' * 256,
    #     difficulty=b'\x00' * 32,
    #     number=b'\x00',
    #     gas_limit=b'\x00' * 32,
    #     gas_used=b'\x00' * 32,
    #     timestamp=b'\x00',
    #     extra_data=b'',
    #     mix_hash=b'\x00' * 32,
    #     nonce=b'\x00',
    # )
    # print("---\n---\n---\n")
    # encoded = encode([sample_header])
    # print("encoded: ", encoded)
    # decoded_rlps = decode(encoded)
    # print(type(decoded_rlps))
    # header1 = decode(encode(decoded_rlps[0]), Header)
    # print(header1)
    # print(int.from_bytes(b'\x98\x96\x80', 'big'))
    # print(b'@\xcfD0\xec\xaas7\x87\xd1\xa6QT\xa3\xb9\xef\xb5`\xc9]\x9e2J#\xb9\x7f\x06\t\xb59\x13;'.hex())

    # in a file write an array of 

if __name__ == '__main__':
    main()