use std::fs;

fn calculate_wrapping_paper(dimensions: &str) -> u32 {
    let dims: Vec<u32> = dimensions.split('x')
        .map(|s| s.parse().unwrap())
        .collect();
    let (l, w, h) = (dims[0], dims[1], dims[2]);
    
    // Calculate surface area
    let surface_area = 2*l*w + 2*w*h + 2*h*l;
    
    // Find smallest side
    let sides = [l*w, w*h, h*l];
    let slack = *sides.iter().min().unwrap();
    
    surface_area + slack
}

fn main() {
    // Test cases with assertions
    assert_eq!(calculate_wrapping_paper("2x3x4"), 58);
    assert_eq!(calculate_wrapping_paper("1x1x10"), 43);
    
    // Read input and calculate total
    let script_dir = std::path::Path::new(file!()).parent().unwrap();
    let input_path = script_dir.join("..").join("input.txt");
    let input = fs::read_to_string(input_path).unwrap();
    let total: u32 = input.lines()
        .filter(|line| !line.is_empty())
        .map(|line| calculate_wrapping_paper(line))
        .sum();
    println!("Rust: {}", total);
}
