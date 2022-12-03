use std::error::Error;
use std::fs;
use std::str::Split;

fn letter_to_points(letter: &str) -> u64 {
    // Rock = 1 ; Paper = 2 ; Scissors = 3
    if letter == "A" || letter == "X" {
        1
    } else if letter == "B" || letter == "Y" {
        2
    } else if letter == "C" || letter == "Z" {
        3
    } else {
        panic!()
    }
}

fn compute_points(duel: [u64; 2]) -> u64 {
    let mut result: i64 = 0;
    result += duel[1] as i64;
    let match_result: i64 = (duel[1] as i64 - duel[0] as i64).rem_euclid(3);
    if match_result == 1 {
        // win
        result += 6;
    } else if match_result == 0 {
        // draw
        result += 3;
    }
    // println!("{} vs {} : result = {} + {} = {}", duel[0], duel[1], duel[1], result - duel[1] as i64, result);
    result as u64
}

fn main() -> Result<(), Box<dyn Error>> {
    // -------- Part 1 ---------
    // let input = fs::read_to_string("src/input/ex02")?;
    let input = fs::read_to_string("src/input/input02")?;
    let input = input.trim();
    // dbg!(&input);
    let input_list = input
        .split("\r\n")
        .map(|e| e.split(" ").collect::<Vec<&str>>().try_into().unwrap());
    // dbg!(&input_list);
    let list_points = input_list.map(|duel: [&str; 2]| duel.map(letter_to_points));
    // dbg!(&list_symbols);
    let part1: u64 = list_points.map(|duel| compute_points(duel)).sum();
    println!("Part 1 : {part1}");

    // -------- Part 2 ---------

    // let input = fs::read_to_string("src/input/ex02")?;
    let input = fs::read_to_string("src/input/input02")?;
    let input = input.trim();
    // dbg!(&input);
    let input_list = input.split("\r\n").map(|e| e.split(" "));
    // dbg!(&input_list);
    fn generate_symbols(duel: Split<&str>) -> [u64; 2] {
        let duel: [&str; 2] = duel.collect::<Vec<&str>>().try_into().unwrap();
        let opponent_shape = letter_to_points(duel[0]);

        match duel[1] {
            "X" => [opponent_shape, (opponent_shape + 1).rem_euclid(3) + 1], // lose
            "Y" => [opponent_shape, opponent_shape],                         // draw
            "Z" => [opponent_shape, opponent_shape.rem_euclid(3) + 1],       // win
            _ => panic!(),
        }
    }
    let list_symbols = input_list.map(generate_symbols);
    // dbg!(&list_symbols);
    let part2: u64 = list_symbols.map(|duel| compute_points(duel)).sum();
    println!("Part 2 : {part2}");

    Ok(())
}
