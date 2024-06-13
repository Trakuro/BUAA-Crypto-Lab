# ECC Basic Calculations
# y^2 = x^3 + ax + b | mod p
# where: 3*a^3 + 27*b^2 != 0

from typing import Tuple

Point = Tuple[int, int]


class EccCurve:
    INFINITY: Point = (0, 0)

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    @staticmethod
    def mod_inverse(a, p):
        if a == 0:
            raise ZeroDivisionError("division by zero")
        lm, hm = 1, 0
        low, high = a % p, p
        while low > 1:
            ratio = high // low
            nm, new = hm - lm * ratio, high - low * ratio
            lm, low, hm, high = nm, new, lm, low
        return lm % p

    def add(self, P: Point, Q: Point) -> Point:
        if P == self.INFINITY:
            return Q

        if Q == self.INFINITY:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and (y1 + y2) % self.p == 0:
            return self.INFINITY

        if P == Q:
            k = (3 * (x2**2) + self.a) * self.mod_inverse(2 * y1, self.p)
        else:
            k = (y2 - y1) * self.mod_inverse(x2 - x1, self.p)

        x3 = int(k**2 - x1 - x2) % self.p
        y3 = int(k * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def negate(self, P):
        x, y = P
        return (x, -y % self.p)

    def multiply(self, k, P):
        result = self.INFINITY
        addend = P

        while k > 0:
            if k & 1:
                result = self.add(result, addend)
            addend = self.add(addend, addend)
            k >>= 1  # 这不是我们bind函数吗 下次转载记得注明出处

        return result


def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = tuple(map(int, input().split()))
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    k = int(input())

    Curve = EccCurve(a, b, p)
    addition = Curve.add(P, Q)
    subtraction = Curve.add(P, Curve.negate(Q))
    multi = Curve.multiply(k, P)

    print(*addition)
    print(*subtraction)
    print(*multi)


if __name__ == "__main__":
    main()
