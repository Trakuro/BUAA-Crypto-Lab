from __future__ import annotations
from typing import Union
from math import gcd


# A simple implementation for matrices modulo 26
# supports __mul__ , inverse and text transformations
class Matrix:
    def __init__(self, data) -> None:
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0]) if data else 0

        # I do not actually accept a 0x0 matrix so...
        assert self.rows > 0
        assert self.columns > 0

    def __mul__(self, other: Union[int, Matrix], /) -> Matrix:
        if isinstance(other, int):
            multiplied_data = [
                [element * other % 26 for element in row] for row in self.data
            ]
            return Matrix(multiplied_data)
        elif isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("Unaccepted size for matrix multiplication.")

            result = []
            for row in self.data:
                result_row = []
                for column in other.transpose().data:
                    result_row.append(sum(a * b for a, b in zip(row, column)) % 26)
                result.append(result_row)

            return Matrix(result)
        else:
            raise TypeError("Unaccepted type for multiplication.")

    def inverse(self) -> Matrix:
        if self.rows != self.columns:
            raise ValueError("Non-square matrix is not invertible.")

        det_val = self.det()
        if det_val == 0:
            raise ValueError("Singular matrix has no inverse.")

        cofactor = self.cofactor()
        adj_cofactor = cofactor.transpose()
        inverse_matrix = adj_cofactor * mod_inv(det_val % 26, 26)

        return inverse_matrix

    def cofactor(self) -> Matrix:
        if self.rows != self.columns:
            raise ValueError("Non-square matrix has no cofactor defined.")

        cofactor = []
        for i in range(self.rows):
            cofactor_row = []
            for j in range(self.columns):
                cofactor_row.append(self.submatrix(i, j).det() * ((-1) ** (i + j)))
            cofactor.append(cofactor_row)

        return Matrix(cofactor)

    def transpose(self) -> Matrix:
        data = self.data
        transposed_data = [list(row) for row in zip(*data)]
        return Matrix(transposed_data)

    def submatrix(self, i, j) -> Matrix:
        if i >= (self.rows) or j >= (self.columns):
            raise ValueError("submatrix index out of bound.")

        submatrix_data = [
            [self.data[row][col] for col in range(self.columns) if col != j]
            for row in range(self.rows)
            if row != i
        ]

        return Matrix(submatrix_data)

    # Determinant of matrix
    def det(self) -> int:
        if self.rows != self.columns:
            raise ValueError("Non-square matrix's determinant is not defined.")

        if self.rows == 1:
            return self.data[0][0]
        elif self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            determinant = 0
            # Expanding the matrix on the first row
            for j in range(self.columns):
                submatrix = self.submatrix(0, j)
                determinant += submatrix.det() * ((-1) ** (j)) * self.data[0][j]

            return determinant

    @classmethod
    def from_text(cls, text: str, block_size: int) -> Matrix:
        data = []
        blocks = [
            text[i * block_size : (i + 1) * block_size]
            for i in range(len(text) // block_size)
        ]
        for block in blocks:
            row = [ord(char) - ord("a") for char in block]
            data.append(row)
        return Matrix(data)

    def to_text(self) -> str:
        result = ""
        for row in self.data:
            for char in row:
                result += chr(char + ord("a"))

        return result


def mod_inv(value: int, modulo: int) -> int:
    if gcd(value, modulo) != 1:
        raise ValueError(
            "Value and modulo must be coprime for modular inverse to exist."
        )

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd_val, x, y = extended_gcd(b % a, a)
            return gcd_val, y - (b // a) * x, x

    gcd_val, x, _ = extended_gcd(value, modulo)
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist.")

    return x % modulo if x >= 0 else (x % modulo + modulo) % modulo


class Hill:
    def __init__(self, key: Matrix) -> None:
        self.enc_matrix = key
        self.dec_matrix = key.inverse()

    def encrypt(self, text: str, block_size: int) -> str:
        text_matrix = Matrix.from_text(text, block_size)
        cipher_matrix = text_matrix * self.enc_matrix
        return cipher_matrix.to_text()

    def decrypt(self, cipher: str, block_size: int) -> str:
        cipher_matrix = Matrix.from_text(cipher, block_size)
        text_matrix = cipher_matrix * self.dec_matrix
        return text_matrix.to_text()


def main():
    block_size = int(input())
    key_matrix = []
    for _ in range(block_size):
        key_row = list(map(int, (input().split())))
        key_matrix.append(key_row)

    text = input().strip()
    mode = int(input())

    hill_cipher = Hill(Matrix(key_matrix))

    if mode:
        print(hill_cipher.encrypt(text, block_size))
    else:
        print(hill_cipher.decrypt(text, block_size))


if __name__ == "__main__":
    main()
