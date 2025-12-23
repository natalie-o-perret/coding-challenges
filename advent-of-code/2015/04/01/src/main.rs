use md5;
use std::fs;

fn find_advent_coin(secret_key: &str) -> u32 {
    let mut number = 1;
    loop {
        let text = format!("{}{}", secret_key, number);
        let digest = md5::compute(text.as_bytes());
        let hash = digest.0;
        // Check if first 2.5 bytes are zero (5 hex digits)
        if hash[0] == 0 && hash[1] == 0 && (hash[2] & 0xF0) == 0 {
            return number;
        }
        number += 1;
    }
}

fn main() {
    // Test cases with assertions
    assert_eq!(find_advent_coin("abcdef"), 609043);
    assert_eq!(find_advent_coin("pqrstuv"), 1048970);

    // Read input and calculate result
    let secret_key = fs::read_to_string("../input.txt")
        .expect("Failed to read input file")
        .trim()
        .to_string();
    
    let result = find_advent_coin(&secret_key);
    println!("Rust: {}", result);
}
