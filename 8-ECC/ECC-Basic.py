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
            k = (3 * x2 + self.a) / (2 * y1)
        else:
            k = (y2 - y1) / (x2 - x1)

        x3 = int(k**2 - x1 - x2) % self.p
        y3 = int(k * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def negate(self, P):
        x, y = P
        return (x, -y % self.p)

    def multiply(self, k, P):
        if k == 0:
            return self.INFINITY
        if k == 1:
            return P
        if k % 2 == 0:
            return self.multiply(k // 2, self.add())


def main():
    p = int(input())
    a = int(input())
    b = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    k = int(input())
