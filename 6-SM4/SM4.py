from enum import Enum


def pkcs(data: bytes, block_size: int = 8):
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)


def left_rotate(data: bytes, shift: int, bit_length: int = 32) -> bytes:
    num = int.from_bytes(data, byteorder="big")
    rotated_num = ((num << shift) & ((1 << bit_length) - 1)) | (num >> (32 - shift))
    return rotated_num.to_bytes(len(data), byteorder="big")


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


class SM4:
    class WorkMode(Enum):
        MODE_ECB = 1
        MODE_CBC = 2
        MODE_CTR = 3
        MODE_CFB = 4
        MODE_OFB = 5

    def __init__(self, key: bytes, mode: WorkMode = WorkMode.MODE_ECB) -> None:
        self.key = key
        self.mode = mode

        assert len(key) == 16
        self.key_expansion()

    def key_expansion(self) -> None:
        # Const Used FK[0-3]
        # FK = [0xA3B1BAC6, 0x56AA3350, 0x677D9197, 0xB27022DC]
        FK = [
            b"\xa3\xb1\xba\xc6",
            b"\x56\xaa\x33\x50",
            b"\x67\x7d\x91\x97",
            b"\xb2\x70\x22\xdc",
        ]

        CK = [
            b"\x00\x07\x0e\x15",
            b"\x1c\x23\x2a\x31",
            b"\x38\x3f\x46\x4d",
            b"\x54\x5b\x62\x69",
            b"\x70\x77\x7e\x85",
            b"\x8c\x93\x9a\xa1",
            b"\xa8\xaf\xb6\xbd",
            b"\xc4\xcb\xd2\xd9",
            b"\xe0\xe7\xee\xf5",
            b"\xfc\x03\x0a\x11",
            b"\x18\x1f\x26\x2d",
            b"\x34\x3b\x42\x49",
            b"\x50\x57\x5e\x65",
            b"\x6c\x73\x7a\x81",
            b"\x88\x8f\x96\x9d",
            b"\xa4\xab\xb2\xb9",
            b"\xc0\xc7\xce\xd5",
            b"\xdc\xe3\xea\xf1",
            b"\xf8\xff\x06\x0d",
            b"\x14\x1b\x22\x29",
            b"\x30\x37\x3e\x45",
            b"\x4c\x53\x5a\x61",
            b"\x68\x6f\x76\x7d",
            b"\x84\x8b\x92\x99",
            b"\xa0\xa7\xae\xb5",
            b"\xbc\xc3\xca\xd1",
            b"\xd8\xdf\xe6\xed",
            b"\xf4\xfb\x02\x09",
            b"\x10\x17\x1e\x25",
            b"\x2c\x33\x3a\x41",
            b"\x48\x4f\x56\x5d",
            b"\x64\x6b\x72\x79",
        ]

        MK = [self.key[i : i + 4] for i in range(0, 16, 4)]
        K = [xor(x, y) for x, y in zip(MK, FK)]  # Generated Key List
        
        for i in range()

    def encrypt(self, data: bytes) -> bytes:
        return b"\xde\xad\xbe\xef"
