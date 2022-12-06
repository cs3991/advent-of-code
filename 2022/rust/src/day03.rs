use std::error::Error;
use std::fs;
use std::time::Instant;

fn priority(character: char) -> u64 {
    match character.is_ascii_lowercase() {
        true => character as u64 - 96,
        false => character as u64 - 65 + 27,
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("Advent of Code 2022 - Jour 03");

    // -------- Part 1 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex03")?;
    let input_str =
        fs::read_to_string("src/input/input03")?;
    let input_str = input_str.trim();
    let backpack_list =
        input_str.lines().map(|backpack_content| {
            [
                backpack_content
                    .get(..backpack_content.len() / 2)
                    .unwrap(),
                backpack_content
                    .get(backpack_content.len() / 2..)
                    .unwrap(),
            ]
        });
    // dbg!(backpack_list.collect::<Vec<[&str; 2]>>());
    let part1: u64 = backpack_list
        .map(|backpack| {
            backpack[0]
                .chars()
                .find(|&character| {
                    backpack[1].contains(character)
                })
                .unwrap()
        })
        .map(priority)
        .sum();
    println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!(
        "Temps d'exécution de la partie 1 : {:?}",
        duration
    );

    // -------- Part 2 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex03")?;
    let input_str =
        fs::read_to_string("src/input/input03")?;
    let input_str = input_str.trim();
    let size = input_str.lines().count();
    assert_eq!(size % 3, 0);
    let mut group_list: Vec<[Option<&str>; 3]> = Vec::new();
    for (i, line) in input_str.lines().enumerate() {
        if i % 3 == 0 {
            group_list.push([None; 3]);
        }
        group_list[i / 3][i % 3] = Some(line);
    }
    let part2: u64 = group_list
        .iter()
        .map(|group| {
            group[0].unwrap().chars().find(|&char| {
                group[1].unwrap().contains(char)
                    && group[2].unwrap().contains(char)
            })
        })
        .map(|char| priority(char.unwrap()))
        .sum();

    println!("Part 2 : {part2}");

    let duration = start.elapsed();
    println!(
        "Temps d'exécution de la partie 2 : {:?}",
        duration
    );
    Ok(())
}

