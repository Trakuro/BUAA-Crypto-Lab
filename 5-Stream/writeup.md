## BBS CSPRBG Crypto Secure Pseudo Random Bit Generator

pick p, q === 3 (mod 4)
n = p*q

pick an random number s, that gcd(s, n) == 1, as seed

x0 = s^2 % n
loop:
    x[i] = x[i-1] ^ 2 % n
    b[i] = x[i] % 2


<!-- yes this is easy to understand. -->

## ANSI
use Triple DES(EDE)

Given timestamp DT, Given seed Vi
two DES keys K1, K2
