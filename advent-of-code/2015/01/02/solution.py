from pathlib import Path


def find_and_print_basement_position(source: str) -> None:
    floor = 0
    for position, char in enumerate(source, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        
        if floor == -1:
            print(position)
            break

# causes him to enter the basement at character position 1
find_and_print_basement_position(")")

# causes him to enter the basement at character position 5
find_and_print_basement_position("()())")

input_file = Path(__file__).parent.parent / "input.txt"
find_and_print_basement_position(input_file.read_text())
