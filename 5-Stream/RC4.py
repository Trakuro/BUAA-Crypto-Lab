import sys


class RC4:
    def __init__(self, key: str) -> None:
        self.key = [int(key[i : i + 2], 16) for i in range(0, len(key), 2)]
        self.key_len = len(self.key)

        # Initialize S-Box using key
        self.s_box = list(range(256))
        j = 0
        for i in range(256):
            j = (j + self.s_box[i] + self.key[i % self.key_len]) % 256
            self.swap(i, j)

        # Initialize the two pointers
        self.i = 0
        self.j = 0

    def swap(self, i: int, j: int) -> None:
        self.s_box[i], self.s_box[j] = self.s_box[j], self.s_box[i]

    # God I must be mad to take down so many self self self self self and self
    # help
    def encrypt(self, input_byte: int) -> int:
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.s_box[self.i]) % 256
        self.swap(self.i, self.j)

        k = self.s_box[(self.s_box[self.i] + self.s_box[self.j]) % 256]
        return input_byte ^ k


def main():
    key = input()[2:]
    this_byte = sys.stdin.read(2)  # Get the 0x from stdin

    rc4 = RC4(key)
    print("0x", end="")
    while True:
        this_byte = sys.stdin.read(2)
        if len(this_byte) < 2:
            break

        try:
            this_char = int(this_byte, 16)
            print(hex(rc4.encrypt(this_char))[2:], end="")
        except ValueError:
            break


if __name__ == "__main__":
    main()
