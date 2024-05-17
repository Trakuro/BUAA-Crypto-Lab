from hashlib import sha1
from typing import Optional

base_message = "The quick brown fox jumps over the lazy dog"


def hash(data: str) -> str:
    return sha1(data.encode()).hexdigest()


def collide(message: str) -> Optional[str]:
    original_hash = hash(message)
    target = original_hash[:8]

    modified_message = message
    for _ in range(1000000):
        modified_message += " "
        if hash(modified_message).startswith(target):
            return modified_message

    return None


if modified_message := collide(base_message):
    print(base_message)
    print(hash(base_message))
    print(modified_message)
    print(hash(modified_message))
else:
    print(None)
