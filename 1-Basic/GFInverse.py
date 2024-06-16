from __future__ import annotations


class GF256:
    def __init__(self, value: int, modulo: int = 0x11B) -> None:
        self.value = value & 0xFF
        self.modulo = modulo

    def __add__(self, other: GF256) -> GF256:
        result = self.value ^ other.value
        return GF256(result, self.modulo)

    def __sub__(self, other: GF256) -> GF256:
        result = self.value ^ other.value
        return GF256(result, self.modulo)

    def __mul__(self, other: GF256) -> GF256:
        result = 0
        modulo = self.modulo
        a, b = self.value, other.value
        while b:
            if b & 1:
                result = result ^ b
            if a & 0x80:
                a = (a << 1) ^ modulo
            else:
                a <<= 1

            b >>= 1

        return GF256(result, self.modulo)

    def __truediv__(self, other: GF256) -> GF256:
        return self * other.inverse()

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, GF256):
            return (self.value == value.value) and (self.modulo == value.modulo)
        return False

    def inverse(self) -> GF256:
        if self.value == 0:
            raise ValueError("No inverse for zero.")

        # Using Extended Euclid Algorithm to find a^-1 mod m
        # Which is a * a^-1 + m * y (which is zero) = 1 mod m
        a, b = self.value, self.modulo
        u, v = 1, 0
        while a != 1:
            j = a.bit_length() - b.bit_length()
            if j < 0:
                a, b = b, a
                u, v = v, u
                j = -j
            a ^= b << j
            u ^= v << j

        return GF256(u, self.modulo)


def main():
    value = int(input(), 16)
    GFValue = GF256(value)
    Inverse = GFValue.inverse()
    print(hex(Inverse.value)[2:])


if __name__ == "__main__":
    main()
