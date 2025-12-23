use std::collections::HashSet;
use std::fs;

fn count_houses_with_robo(directions: &str) -> usize {
    let mut santa_x = 0;
    let mut santa_y = 0;
    let mut robo_x = 0;
    let mut robo_y = 0;
    let mut visited = HashSet::new();
    visited.insert((0, 0));
    
    for (i, c) in directions.chars().enumerate() {
        if i % 2 == 0 { // Santa's turn
            match c {
                '^' => santa_y += 1,
                'v' => santa_y -= 1,
                '>' => santa_x += 1,
                '<' => santa_x -= 1,
                _ => {}
            }
            visited.insert((santa_x, santa_y));
        } else { // Robo-Santa's turn
            match c {
                '^' => robo_y += 1,
                'v' => robo_y -= 1,
                '>' => robo_x += 1,
                '<' => robo_x -= 1,
                _ => {}
            }
            visited.insert((robo_x, robo_y));
        }
    }
    
    visited.len()
}

fn main() {
    // Test cases with assertions
    assert_eq!(count_houses_with_robo("^v"), 3);
    assert_eq!(count_houses_with_robo("^>v<"), 3);
    assert_eq!(count_houses_with_robo("^v^v^v^v^v"), 11);

    // Read input and calculate result
    let directions = fs::read_to_string("../input.txt")
        .expect("Failed to read input file")
        .trim()
        .to_string();
    
    let result = count_houses_with_robo(&directions);
    println!("Rust: {}", result);
}
