from hashlib import sha256

m = input().strip()
n = int(input()) # RSA modulo
em_bits = int(input())
mode = input().strip()

def mgf(data, length):


def hash_em(message, salt):
    pass


if mode == "Sign":
    d = int(input()) # Private key
    salt = int(input(), 16)


elif mode == "Vrfy":
    e = int(input()) # Public key
    sign = int(input(), 16)

else:
    raise ValueError("Invalid mode")
