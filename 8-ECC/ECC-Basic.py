# ECC Basic Calculations
# y^2 = x^3 + ax + b | mod p
# where: 3*a^3 + 27*b^2 != 0

class EccCurve:
    INFINITY = (0, 0)

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def add(self, P, Q):
        if P == self.INFINITY:
            return Q
        elif Q == self.INFINITY:
            return P
        elif P == Q:
            x, y = P
            k = (3 * x + self.a) / (2 * y)
            x3 = (k ** 2 - 2 * x) % self.p
            y3 = (k * (x - x3) - y) % self.p
        else:
            x1, y2 = P
            x2, y2 = Q
            k = (y2 - y1) / (x2 - x1)
            x3 = 


    def negate(self, P):
        x, y = P
        return (x, -y % self.p) 

    def multiply(self, k, P):
        pass



def main():
    p = int(input())
    a = int(input())
    b = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    k = int(input())

