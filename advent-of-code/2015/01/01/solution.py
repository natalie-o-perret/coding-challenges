from functools import reduce
from pathlib import Path


def calculate_floor(source: str) -> int:
    return reduce(lambda floor, character: 
        floor + 1 if character == '(' else 
        floor - 1 if character == ')' else 
        floor, source, 0)

# Test cases with assertions
assert calculate_floor("(())") == 0
assert calculate_floor("()()") == 0
assert calculate_floor("(((") == 3
assert calculate_floor("(()(()(") == 3
assert calculate_floor("))(((((") == 3
assert calculate_floor("())") == -1
assert calculate_floor("))(") == -1
assert calculate_floor(")))") == -3
assert calculate_floor(")())())") == -3

# Calculate and print the answer
input_file = Path(__file__).parent.parent / "input.txt"
print(f"Python: {calculate_floor(input_file.read_text())}")
