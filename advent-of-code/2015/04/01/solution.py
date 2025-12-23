import hashlib
import os

def find_advent_coin(secret_key):
    number = 1
    while True:
        text = secret_key + str(number)
        hash_bytes = hashlib.md5(text.encode()).digest()
        # Check if first 2.5 bytes are zero (5 hex digits)
        if hash_bytes[0] == 0 and hash_bytes[1] == 0 and (hash_bytes[2] & 0xF0) == 0:
            return number
        number += 1

# Test cases with assertions
assert find_advent_coin("abcdef") == 609043
assert find_advent_coin("pqrstuv") == 1048970

# Read input and calculate result
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "..", "input.txt")
with open(input_path) as f:
    secret_key = f.read().strip()

result = find_advent_coin(secret_key)
print(f"Python: {result}")
