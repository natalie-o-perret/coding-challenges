use std::fs;

fn calculate_and_print_floor(source: &str) {
    let floor = source.chars().fold(0, |floor, character| match character {
        '(' => floor + 1,
        ')' => floor - 1,
        _ => floor,
    });
    println!("{}", floor);
}

fn main() {
    // both result in floor 0
    calculate_and_print_floor("(())");
    calculate_and_print_floor("()()");

    // both result in floor 3.
    calculate_and_print_floor("(((");
    calculate_and_print_floor("(()(()("  );

    // also results in floor 3.
    calculate_and_print_floor("))((((("  );

    // both result in floor -1 (the first basement level).
    calculate_and_print_floor("())");
    calculate_and_print_floor("))(");

    // both result in floor -3.
    calculate_and_print_floor(")))");
    calculate_and_print_floor(")())())");

    let script_dir = std::path::Path::new(file!()).parent().unwrap();
    let input_path = script_dir.join("..").join("input.txt");
    let input = fs::read_to_string(input_path).unwrap();
    calculate_and_print_floor(&input);
}
