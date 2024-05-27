from Crypto.Cipher import DES3


# Use of some Closure here
# Well it's nonsense i fear
def init(key1: int, key2: int):
    key1_bytes = key1.to_bytes(8, byteorder="big")
    key2_bytes = key2.to_bytes(8, byteorder="big")
    full_key = key1_bytes + key2_bytes + key1_bytes

    def encrypt(plaintext: int) -> int:
        des3 = DES3.new(full_key, DES3.MODE_ECB)
        plaintext_bytes = plaintext.to_bytes(8, byteorder="big")
        return int.from_bytes(des3.encrypt(plaintext_bytes), byteorder="big")

    return encrypt


def main():
    init_vector = int(input(), 16)
    key1 = int(input(), 16)
    key2 = int(input(), 16)
    n = int(input())

    encrypt = init(key1, key2)

    for _ in range(n):
        timestamp = int(input(), 16)
        tmp = encrypt(timestamp)
        ri = encrypt(tmp ^ init_vector)
        print(hex(ri))
        init_vector = encrypt(tmp ^ ri)


if __name__ == "__main__":
    main()
