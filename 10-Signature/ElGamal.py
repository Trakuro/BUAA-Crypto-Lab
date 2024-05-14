from hashlib import sha256

p = int(input()) # Prime Chosen
g = int(input()) # Primitive Root
m = input().encode() # Message
hash_obj = sha256(m)
hash = int.from_bytes(hash_obj.digest(), 'big')
mode = input()

if mode == "Sign":
    x = int(input()) # Private Key
    k = int(input()) # Random Generated k

    r = pow(g, k, p)
    s = (hash - x * r) * pow(k, p-1, p) % (p-1)

    print(r, s)

elif mode == "Vrfy":
    y = int(input()) # Public Key
    r, s = tuple(map(int, input().split()))

    if pow(g, hash, p) == (pow(y, r, p) * pow(r, s, p)) % p:
        print("True")
    else:
        print("False")

else:
    raise ValueError
