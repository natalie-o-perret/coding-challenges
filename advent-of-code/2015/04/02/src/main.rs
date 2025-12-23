use md5;
use std::fs;

fn find_advent_coin(secret_key: &str) -> u32 {
    let mut number = 1;
    loop {
        let text = format!("{}{}", secret_key, number);
        let digest = md5::compute(text.as_bytes());
        let hash = digest.0;
        // Check if first 3 bytes are zero (6 hex digits)
        if hash[0] == 0 && hash[1] == 0 && hash[2] == 0 {
            return number;
        }
        number += 1;
    }
}

fn main() {
    // Test cases - skipped for Part 2 (would take too long)

    // Read input and calculate result
    let secret_key = fs::read_to_string("../input.txt")
        .expect("Failed to read input file")
        .trim()
        .to_string();
    
    let result = find_advent_coin(&secret_key);
    println!("Rust: {}", result);
}
