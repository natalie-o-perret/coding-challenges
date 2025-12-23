use std::fs;

fn is_nice(s: &str) -> bool {
    // Check for a pair that appears at least twice without overlapping
    let has_pair = (0..s.len()-1).any(|i| {
        let pair = &s[i..i+2];
        s[i+2..].contains(pair)
    });
    
    if !has_pair {
        return false;
    }

    // Check for a letter that repeats with exactly one letter between
    let has_repeat = (0..s.len()-2).any(|i| {
        s.as_bytes()[i] == s.as_bytes()[i+2]
    });

    has_repeat
}

fn main() {
    // Test cases with assertions
    assert_eq!(is_nice("qjhvhtzxzqqjkmpb"), true);
    assert_eq!(is_nice("xxyxx"), true);
    assert_eq!(is_nice("uurcxstgmygtbstg"), false);
    assert_eq!(is_nice("ieodomkazucvgmuy"), false);

    // Read input and calculate result
    let content = fs::read_to_string("../input.txt")
        .expect("Failed to read input file");
    
    let count = content.lines().filter(|&s| is_nice(s)).count();
    println!("Rust: {}", count);
}
