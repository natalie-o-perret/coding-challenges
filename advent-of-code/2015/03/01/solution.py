import os

def count_houses(directions):
    x, y = 0, 0
    visited = {(0, 0)}
    
    for char in directions:
        if char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1
        visited.add((x, y))
    
    return len(visited)

# Test cases with assertions
assert count_houses(">") == 2
assert count_houses("^>v<") == 4
assert count_houses("^v^v^v^v^v") == 2

# Read input and calculate result
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "..", "input.txt")
with open(input_path) as f:
    directions = f.read().strip()

result = count_houses(directions)
print(f"Python: {result}")
