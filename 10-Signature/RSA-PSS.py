from hashlib import sha1
from math import ceil
from sys import byteorder

m = input().strip()
n = int(input()) # RSA modulo
em_bits = int(input())
mode = input().strip()

# Meta
emlen = ceil(em_bits / 8)
slen = 20 # Salt length
hlen = 20 # Hash length

def mgf(data: bytes, length: int) -> bytes:
    # Initialize
    T = b""
    counter = 0

    while len(T) < length:
        block = data + counter.to_bytes(4, byteorder="big")
        T += sha1(block).digest()[:hlen]
        counter += 1

    return T[:length]


if mode == "Sign":
    d = int(input()) # Private key
    salt = bytes.fromhex(input()) 

    message_hash = sha1(m.encode()).digest()
    padding_1 = b"\x00" * 8
    modified_message = padding_1 + message_hash + salt
    modified_hash = sha1(modified_message).digest()

    padding_2 = b"\x00" * (emlen - slen - hlen - 2) + b"\x01"
    data_block = padding_2 + salt

    hash_mask = mgf(modified_hash, emlen-hlen-1)
    masked_db = bytes([a ^ b for a, b in zip(data_block, hash_mask)]) 

    encrypted_message = masked_db + modified_hash + b"\xbc"

    plaintext = int.from_bytes(encrypted_message, byteorder="big")
    cipher = pow(plaintext, d, n)

    print(hex(cipher)[2:])


elif mode == "Vrfy":
    try:
        e = int(input()) # Public key
        sign = int(input(), 16)
        plaintext = pow(sign, e, n)
        encrypted_message = plaintext.to_bytes(emlen, byteorder = "big")

        assert encrypted_message.endswith(b"\xbc")
        assert not emlen < hlen + slen + 1

        message_hash = sha1(m.encode()).digest()

        masked_db = encrypted_message[:emlen-hlen-1]
        modified_hash = encrypted_message[emlen-hlen-1:emlen-1]

        assert not masked_db[0] & (0xff << (em_bits - emlen * 8 + 8) )

        db_mask = mgf(modified_hash, emlen-hlen-1)

        data_block = bytes([a ^ b for a, b in zip(masked_db, db_mask)]) 
        data_block = (data_block[0] & (0xff >> (8*emlen-em_bits))).to_bytes(1, byteorder="big") + data_block[1:]

        padding_2 = b"\x00" * (emlen - slen - hlen - 2) + b"\x01"

        assert data_block[:emlen-hlen-slen-1] == padding_2

        salt = data_block[-slen:]
        padding_1 = b"\x00" * 8
        modified_message = padding_1 + message_hash + salt

        verify_hash = sha1(modified_message).digest()

        print(verify_hash == modified_hash)

    except AssertionError:
        print(False)

else:
    raise ValueError("Invalid mode")
