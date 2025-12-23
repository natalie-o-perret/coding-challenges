from pathlib import Path


def find_basement_position(source: str) -> int:
    """
    Finds the position at which the floor first reaches the basement.
    Returns the 1-based position where the cumulative floor value first becomes -1.
    If the basement is never reached, returns 0.
    """
    floor = 0
    for position, char in enumerate(source, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        
        if floor == -1:
            return position
    return 0

# Test cases with assertions
assert find_basement_position(")") == 1
assert find_basement_position("()())") == 5

# Calculate and print the answer
input_file = Path(__file__).parent.parent / "input.txt"
print(f"Python: {find_basement_position(input_file.read_text())}")
