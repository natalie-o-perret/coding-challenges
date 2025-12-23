from pathlib import Path


def calculate_wrapping_paper(dimensions):
    """Calculate wrapping paper needed for a present."""
    l, w, h = map(int, dimensions.split('x'))
    
    # Calculate surface area
    surface_area = 2*l*w + 2*w*h + 2*h*l
    
    # Find smallest side
    sides = [l*w, w*h, h*l]
    slack = min(sides)
    
    return surface_area + slack

# Test cases with assertions
assert calculate_wrapping_paper("2x3x4") == 58
assert calculate_wrapping_paper("1x1x10") == 43

# Read input and calculate total
input_file = Path(__file__).parent.parent / "input.txt"
total = sum(calculate_wrapping_paper(line.strip()) for line in input_file.read_text().splitlines() if line.strip())
print(f"Python: {total}")
