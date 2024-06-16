# Columnar Transposition Cipher
# class CTC:
#     def __init__(self, key: str) -> None:
#         self.key = key
#

# OK Fine I find this cipher completely meaningless
# So I decided to work it on the easiest way.
# GTFO


block_size = int(input())
key = input().strip()
text = input().strip()
mode = int(input())

order = [int(x) - 1 for x in key]


def permute(lst, order):
    return [lst[i] for i in order]


def real_permute(lst, order):
    result = [""] * block_size
    for idx, item in zip(order, lst):
        result[idx] = item

    return result


if mode:
    table = [[]] * block_size
    text_blocks = [text[i : block_size + i] for i in range(0, len(text), block_size)]
    print(text_blocks)
    for block in text_blocks:
        for idx, char in enumerate(block):
            table[idx].append(char)

    print(table)
    table = real_permute(table, order)
    print(table)
    cipher = "".join([y for x in table for y in x])
    print(cipher)
