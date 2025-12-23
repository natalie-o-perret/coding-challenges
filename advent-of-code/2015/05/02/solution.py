import os

def is_nice(string):
    # Check for a pair that appears at least twice without overlapping
    has_pair = False
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        # Look for the same pair starting at least 2 positions later
        if pair in string[i+2:]:
            has_pair = True
            break
    
    if not has_pair:
        return False
    
    # Check for a letter that repeats with exactly one letter between
    has_repeat = any(string[i] == string[i+2] for i in range(len(string)-2))
    
    return has_repeat

# Test cases with assertions
assert is_nice("qjhvhtzxzqqjkmpb") == True
assert is_nice("xxyxx") == True
assert is_nice("uurcxstgmygtbstg") == False
assert is_nice("ieodomkazucvgmuy") == False

# Read input and calculate result
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "..", "input.txt")
with open(input_path) as f:
    strings = f.read().strip().split('\n')

result = sum(1 for s in strings if is_nice(s))
print(f"Python: {result}")
