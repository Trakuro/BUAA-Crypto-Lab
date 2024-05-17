from typing import Union


def left_rotate(value, bits):
    return ((value << bits) | (value >> (32 - bits))) & 0xFFFFFFFF


def sha1(data: Union[bytes, bytearray]) -> str:
    # Initialization
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Padding
    length = len(data) * 8
    data += b"\x80"
    while (len(data) * 8) % 512 != 448:
        data += b"\x00"
    data += length.to_bytes(8, byteorder="big")

    # Break in to 64 byte chunks
    chunks = [data[i : i + 64] for i in range(0, len(data), 64)]

    # Process
    digest = ""

    for chunk in chunks:
        words = []
        for i in range(16):
            words.append(int.from_bytes(chunk[i * 4 : (i + 1) * 4], byteorder="big"))

        for i in range(16, 80):
            words.append(
                left_rotate(
                    words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1
                )
            )

        # initial value for this chunk:
        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if i in range(20):
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i in range(20, 40):
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i in range(40, 60):
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + words[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (a + h0) & 0xFFFFFFFF
        h1 = (b + h1) & 0xFFFFFFFF
        h2 = (c + h2) & 0xFFFFFFFF
        h3 = (d + h3) & 0xFFFFFFFF
        h4 = (e + h4) & 0xFFFFFFFF

    digest = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return "{:040x}".format(digest)


s = input()
print(sha1(s.encode()))
