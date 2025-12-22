from functools import reduce

from pathlib import Path


def calculate_and_print_floor(source: str) -> None:
    floor: int = reduce(lambda floor, character: 
        floor + 1 if character == '(' else 
        floor - 1 if character == ')' else 
        floor, source, 0)
    print(floor)

# both result in floor 0
calculate_and_print_floor("(())")
calculate_and_print_floor("()()")

# both result in floor 3.
calculate_and_print_floor("(((")
calculate_and_print_floor("(()(()("  )

# also results in floor 3.
calculate_and_print_floor("))((((("  )

# both result in floor -1 (the first basement level).
calculate_and_print_floor("())")
calculate_and_print_floor("))(")

# both result in floor -3.
calculate_and_print_floor(")))")
calculate_and_print_floor(")())())")

input_file = Path(__file__).parent.parent / "input.txt"
calculate_and_print_floor(input_file.read_text())
