from hashlib import sha1

p = int(input())  # prime number
q = int(input())  # where p = qr + 1
g = int(input())  # primitive root
m = input()
mode = input()

if mode == "Sign":
    x = int(input())  # Private Key
    k = int(input())  # Randomly Generated k

    r = pow(g, k, p)

    e = int(sha1((m + str(r)).encode()).hexdigest(), 16)
    s = (k + x * e) % q

    print(e, s)

elif mode == "Vrfy":
    y = int(input())  # Public Key
    e, s = tuple(map(int, input().split()))

    r = pow(g, s, p) * pow(y, e, p) % p
    my_hash = int(sha1((m + str(r)).encode()).hexdigest(), 16)

    print(e == my_hash)

else:
    raise ValueError("Invalid mode.")
