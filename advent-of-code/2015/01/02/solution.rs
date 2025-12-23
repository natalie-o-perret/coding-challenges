use std::fs;

fn find_basement_position(source: &str) -> usize {
    let mut floor = 0;
    for (position, character) in source.chars().enumerate() {
        match character {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }

        if floor == -1 {
            return position + 1; // 1-indexed
        }
    }
    0
}

fn main() {
    // Test cases with assertions
    assert_eq!(find_basement_position(")"), 1);
    assert_eq!(find_basement_position("()())"), 5);

    // Calculate and print the answer
    let script_dir = std::path::Path::new(file!()).parent().unwrap();
    let input_path = script_dir.join("..").join("input.txt");
    let instructions = fs::read_to_string(input_path).unwrap();
    println!("Rust: {}", find_basement_position(&instructions));
}
