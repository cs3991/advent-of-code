use std::fs;
use std::time::Instant;


fn is_all_different<T: PartialEq>(list: &Vec<T>) -> bool {
    for (i, e) in list.iter().enumerate() {
        if list[i + 1..].contains(e) {
            return false;
        }
    }
    true
}

fn main() {
    println!("Advent of Code 2022 - Jour 06");

    // -------- Part 1 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex06").unwrap();
    let input_str = fs::read_to_string("src/input/input06").unwrap();
    let input_str = input_str.trim();
    let mut last_chars: Vec<char> = input_str.chars().take(4).collect();
    let mut i = 0;
    for c in input_str.chars() {
        last_chars.push(c);
        last_chars.remove(0);
        // dbg!(&last_chars);
        i += 1;
        if is_all_different(&last_chars) {
            break;
        }
    }
    if !is_all_different(&last_chars) {
        panic!("Non trouvé");
    }

    println!("Part 1 : {}", i);

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 1 : {:?}", duration);

    // -------- Part 2 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex06").unwrap();
    let input_str = fs::read_to_string("src/input/input06").unwrap();
    let input_str = input_str.trim();
    let mut last_chars: Vec<char> = input_str.chars().take(14).collect();
    let mut i = 0;
    for c in input_str.chars() {
        last_chars.push(c);
        last_chars.remove(0);
        // dbg!(&last_chars);
        i += 1;
        if is_all_different(&last_chars) {
            break;
        }
    }
    if !is_all_different(&last_chars) {
        panic!("Non trouvé");
    }

    println!("Part 2 : {}", i);

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 2 : {:?}", duration);
}
