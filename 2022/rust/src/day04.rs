use std::error::Error;
use std::fs;
use std::time::Instant;

fn main() -> Result<(), Box<dyn Error>> {
    println!("Advent of Code 2022 - Jour 04");

    // -------- Part 1 ---------
    let start = Instant::now();

    // let input_str = fs::read_to_string("src/input/ex04")?;
    let input_str = fs::read_to_string("src/input/input04")?;
    let input_str = input_str.trim();
    let part1: u64 = input_str
        .lines()
        .map(|pair| {
            let mut pair = pair.split(&['-', ','][..]);
            [
                [
                    pair.next().unwrap().parse().unwrap(),
                    pair.next().unwrap().parse().unwrap(),
                ],
                [
                    pair.next().unwrap().parse().unwrap(),
                    pair.next().unwrap().parse().unwrap(),
                ],
            ]
        })
        .map(|pair: [[u64; 2]; 2]| {
            // 1ere range incluse dans la seconde
            match (pair[0][0] <= pair[1][0] && pair[0][1] >= pair[1][1])
                // 2eme range incluse dans la première
                || (pair[0][0] >= pair[1][0] && pair[0][1] <= pair[1][1])
            {
                true => 1,
                false => 0,
            }
        })
        .sum();
    println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 1 : {:?}", duration);

    // -------- Part 2 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex04")?;
    let input_str = fs::read_to_string("src/input/input04")?;
    let input_str = input_str.trim();
    let part2: u64 = input_str
        .lines()
        .map(|pair| {
            let mut pair = pair.split(&['-', ','][..]);
            [
                [
                    pair.next().unwrap().parse().unwrap(),
                    pair.next().unwrap().parse().unwrap(),
                ],
                [
                    pair.next().unwrap().parse().unwrap(),
                    pair.next().unwrap().parse().unwrap(),
                ],
            ]
        })
        .map(|pair: [[u64; 2]; 2]| {
            match (pair[0][0] <= pair[1][1] && pair[0][1] >= pair[1][0])
                || (pair[0][0] >= pair[1][1] && pair[0][1] <= pair[1][0])
            {
                true => 1,
                false => 0,
            }
        })
        .sum();
    println!("Part 1 : {part2}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 2 : {:?}", duration);
    Ok(())
}

