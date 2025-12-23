use std::collections::HashSet;
use std::fs;

fn count_houses(directions: &str) -> usize {
    let mut x = 0;
    let mut y = 0;
    let mut visited = HashSet::new();
    visited.insert((0, 0));
    
    for c in directions.chars() {
        match c {
            '^' => y += 1,
            'v' => y -= 1,
            '>' => x += 1,
            '<' => x -= 1,
            _ => {}
        }
        visited.insert((x, y));
    }
    
    visited.len()
}

fn main() {
    // Test cases with assertions
    assert_eq!(count_houses(">"), 2);
    assert_eq!(count_houses("^>v<"), 4);
    assert_eq!(count_houses("^v^v^v^v^v"), 2);

    // Read input and calculate result
    let directions = fs::read_to_string("../input.txt")
        .expect("Failed to read input file")
        .trim()
        .to_string();
    
    let result = count_houses(&directions);
    println!("Rust: {}", result);
}
