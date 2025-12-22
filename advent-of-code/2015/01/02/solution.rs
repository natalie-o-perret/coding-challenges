use std::fs;

fn find_and_print_basement_position(source: &str) {
    let mut floor = 0;
    for (position, character) in source.chars().enumerate() {
        match character {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }

        if floor == -1 {
            println!("{}", position + 1); // 1-indexed
            break;
        }
    }
}

fn main() {
    // causes him to enter the basement at character position 1
    find_and_print_basement_position(")");

    // causes him to enter the basement at character position 5
    find_and_print_basement_position("()())");

    let instructions = fs::read_to_string("../input.txt")
        .expect("Failed to read input file");
    find_and_print_basement_position(&instructions);
}
