use std::error::Error;
use std::fs;
use std::str::Split;
use std::time::Instant;

fn main() {
    println!("Advent of Code 2022 - Jour XX");

    // -------- Part 1 ---------
    let start = Instant::now();
    let input_str = fs::read_to_string("src/input/exXX").unwrap();
    // let input_str = fs::read_to_string("src/input/inputXX").unwrap();
    let input_str = input_str.trim();

    // println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!(
        "Temps d'exécution de la partie 1 : {:?}",
        duration
    );

    // -------- Part 2 ---------
    let start = Instant::now();
    let input_str = fs::read_to_string("src/input/exXX").unwrap();
    // let input_str = fs::read_to_string("src/input/inputXX").unwrap();
    let input_str = input_str.trim();

    // println!("Part 2 : {part2}");

    let duration = start.elapsed();
    println!(
        "Temps d'exécution de la partie 2 : {:?}",
        duration
    );
}
