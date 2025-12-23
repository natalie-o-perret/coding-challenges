use std::fs;

fn calculate_ribbon(dimensions: &str) -> u32 {
    let mut dims: Vec<u32> = dimensions.split('x')
        .map(|s| s.parse().unwrap())
        .collect();
    dims.sort();
    
    // Smallest perimeter (using two smallest dimensions)
    let perimeter = 2 * (dims[0] + dims[1]);
    
    // Volume for bow
    let volume = dims[0] * dims[1] * dims[2];
    
    perimeter + volume
}

fn main() {
    // Test cases with assertions
    assert_eq!(calculate_ribbon("2x3x4"), 34);
    assert_eq!(calculate_ribbon("1x1x10"), 14);
    
    // Read input and calculate total
    let script_dir = std::path::Path::new(file!()).parent().unwrap();
    let input_path = script_dir.join("..").join("input.txt");
    let input = fs::read_to_string(input_path).unwrap();
    let total: u32 = input.lines()
        .filter(|line| !line.is_empty())
        .map(|line| calculate_ribbon(line))
        .sum();
    println!("Rust: {}", total);
}
