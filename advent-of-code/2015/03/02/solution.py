import os

def count_houses_with_robo(directions):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited = {(0, 0)}
    
    for i, char in enumerate(directions):
        if i % 2 == 0:  # Santa's turn
            if char == '^':
                santa_y += 1
            elif char == 'v':
                santa_y -= 1
            elif char == '>':
                santa_x += 1
            elif char == '<':
                santa_x -= 1
            visited.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if char == '^':
                robo_y += 1
            elif char == 'v':
                robo_y -= 1
            elif char == '>':
                robo_x += 1
            elif char == '<':
                robo_x -= 1
            visited.add((robo_x, robo_y))
    
    return len(visited)

# Test cases with assertions
assert count_houses_with_robo("^v") == 3
assert count_houses_with_robo("^>v<") == 3
assert count_houses_with_robo("^v^v^v^v^v") == 11

# Read input and calculate result
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "..", "input.txt")
with open(input_path) as f:
    directions = f.read().strip()

result = count_houses_with_robo(directions)
print(f"Python: {result}")
