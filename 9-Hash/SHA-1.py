from typing import Union

def left_rotate(value, bits):
    return (value << bits) | (value >> (32 - bits)) & 0xffffffff

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

    # Break in to 64 byte chunks
    chunks = []
    while data:
        chunks.append(data[:64])
        data = data[64:]

    # Process
    digest = ""
    
    for chunk in chunks:
        words = []
        for i in range(16):
            words.append(int.from_bytes(chunk[i*4:(i+1)*4], byteorder = "big"))

        for i in range(16,80):
            words.append(left_rotate(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1))

        # initial value for this chunk:
        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if i in range(20):
                f = (b & c) | ((~b) & d) 
                k = 0x5a827999
            elif i in range(20,40):
                f = b ^ c ^ d
                k = 0x6ed9eba1
            elif i in range(40,60):
                f = (b & c) | (b & d) | (c & d)
                k = 0x8f1bbcdc
            elif i in range(60,80):
                f = b ^ c ^ d
                k = 0xc162c1d6

            temp = left_rotate(a, 5) + f + e + k + words[i]
            e = d
            d = c 
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = ( a + h0 ) % 2 ** 32
        h1 = ( b + h1 ) % 2 ** 32 
        h2 = ( c + h2 ) % 2 ** 32 
        h3 = ( d + h3 ) % 2 ** 32 
        h4 = ( e + h4 ) % 2 ** 32 

    digest = hex(h0)[2:] + hex(h1)[2:] + hex(h2)[2:] + hex(h3)[2:] + hex(h4)[2:]
    return digest

s = input()
print(sha1(s.encode()))



    
