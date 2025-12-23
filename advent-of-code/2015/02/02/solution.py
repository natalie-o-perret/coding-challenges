from pathlib import Path


def calculate_ribbon(dimensions):
    """Calculate ribbon needed for a present."""
    dims = sorted(map(int, dimensions.split('x')))
    
    # Smallest perimeter (using two smallest dimensions)
    perimeter = 2 * (dims[0] + dims[1])
    
    # Volume for bow
    volume = dims[0] * dims[1] * dims[2]
    
    return perimeter + volume

# Test cases with assertions
assert calculate_ribbon("2x3x4") == 34
assert calculate_ribbon("1x1x10") == 14

# Read input and calculate total
input_file = Path(__file__).parent.parent / "input.txt"
total = sum(calculate_ribbon(line.strip()) for line in input_file.read_text().splitlines() if line.strip())
print(f"Python: {total}")
