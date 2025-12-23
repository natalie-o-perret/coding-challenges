use std::fs;

fn calculate_floor(source: &str) -> i32 {
    source.chars().fold(0, |floor, character| match character {
        '(' => floor + 1,
        ')' => floor - 1,
        _ => floor,
    })
}

fn main() {
    // Test cases with assertions
    assert_eq!(calculate_floor("(())"), 0);
    assert_eq!(calculate_floor("()()"), 0);
    assert_eq!(calculate_floor("((("), 3);
    assert_eq!(calculate_floor("(()(()("), 3);
    assert_eq!(calculate_floor("))((((("), 3);
    assert_eq!(calculate_floor("())"), -1);
    assert_eq!(calculate_floor("))("), -1);
    assert_eq!(calculate_floor(")))"), -3);
    assert_eq!(calculate_floor(")())())"), -3);

    // Calculate and print the answer
    let script_dir = std::path::Path::new(file!()).parent().unwrap();
    let input_path = script_dir.join("..").join("input.txt");
    let input = fs::read_to_string(input_path).unwrap();
    println!("Rust: {}", calculate_floor(&input));
}
