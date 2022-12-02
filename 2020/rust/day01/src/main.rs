extern crate core;

use std::fs;

fn main() {
    let input = fs::read_to_string("src/input.txt")
        .expect("Impossible de lire le fichier input.txt");
    let input_lines = input.lines();
    let input_list = input_lines.collect::<Vec<&str>>();
    let mut input_list_int: Vec<i32> = Vec::new();
    for e in input_list {
        input_list_int.push(e.parse::<i32>().unwrap())
    }
    println!("Input : {:?}", input_list_int);

    'outer: for (i, x) in (&input_list_int).iter().enumerate() {
        for y in &input_list_int[i + 1..] {
            if x + y == 2020 {
                println!("Réponse partie 1 : {}", (x * y).to_string());
                break 'outer;
            }
        }
    }

    'outer: for (i, x) in (&input_list_int).iter().enumerate() {
        for (j, y) in (&input_list_int[i + 1..]).iter().enumerate() {
            for z in &input_list_int[j + 1..] {
                if x + y + z == 2020 {
                    println!("Réponse partie 2 : {}", (x * y * z).to_string());
                    break 'outer;
                }
            }
        }
    }
}
