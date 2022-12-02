use std::error::Error;
use std::fs;


fn main() -> Result<(), Box<dyn Error>> {

    // -------- Part 1 ---------
    let input = fs::read_to_string("src/input/input01")?;
    let input = input.trim();
    // dbg!(&input);
    // On utilise &str car c'est des slices. La propriété reste à input
    let elves_str_list: Vec<&str> = input.split("\r\n\r\n").collect();
    // dbg!(&elves_str_list);
    // iter() à enlever plus tard
    let elves_carrying_list: Vec<Vec<u64>> = elves_str_list
        .iter()
        .map(|e| e.split("\r\n").map(|i| i.parse().unwrap()).collect())
        .collect();
    // dbg!(&elves_carrying_list);
    let mut elves_total_cal_list = elves_carrying_list.iter().map(|e| e.iter().sum()).collect::<Vec<u64>>();
    let max_carrying: u64 = *elves_total_cal_list.iter().max().unwrap();
    println!("Partie 1 : {max_carrying}");

    // -------- Part 2 ---------
    elves_total_cal_list.sort();

    let result_part_2: u64 = elves_total_cal_list[elves_total_cal_list.len() - 3 .. elves_carrying_list.len()].iter().sum();
    println!("Partie 2 : {result_part_2}");
    Ok(())
}
