from hashlib import sha256

p = int(input())  # Prime Chosen
g = int(input())  # Primitive Root
m = input().encode()  # Message
hash_obj = sha256(m)
hash = int.from_bytes(hash_obj.digest(), "big")
mode = input()


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_gcd(b, a % b)
        return y, x - (a // b) * y, gcd


def mod_inverse(k, p):
    assert gcd(k, p) == 1

    x, _, _ = extended_gcd(k, p)
    return x % p


if mode == "Sign":
    x = int(input())  # Private Key
    k = int(input())  # Random Generated k

    r = pow(g, k, p)
    s = (hash - x * r) * mod_inverse(k, p - 1) % (p - 1)

    print(r, s)

elif mode == "Vrfy":
    y = int(input())  # Public Key
    r, s = tuple(map(int, input().split()))

    if pow(g, hash, p) == (pow(y, r, p) * pow(r, s, p)) % p:
        print("True")
    else:
        print("False")

else:
    raise ValueError
