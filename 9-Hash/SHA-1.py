from typing import Union


def sha1(data: Union[bytes, bytearray]) -> bytes:

    # Initialization
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Padding
    data += b'\x80'
    while len(data) % 64 != 56:
        data += b'\x00'
    data += len(data).to_bytes(8, byteorder="big")

    
