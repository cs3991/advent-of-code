use regex::Regex;
use std::fs;
use std::time::Instant;

fn main() {
    println!("Advent of Code 2022 - Jour 05");

    // -------- Part 1 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex05").unwrap();
    let input_str = fs::read_to_string("src/input/input05").unwrap();
    let re = Regex::new("\n\n|\r\n\r\n").unwrap();
    let mut split = re.split(&*input_str);
    let (input_str_stacks, input_str_operations): (&str, &str) =
        (split.next().unwrap(), split.next().unwrap());

    // process the stacks map
    let stack_map_tr = input_str_stacks
        .split_once(" 1")
        .unwrap()
        .0
        .lines()
        .rev()
        .map(|line| line.chars().skip(1).step_by(4).collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();
    // dbg!(&stack_map_tr);
    let mut stack_map: Vec<Vec<&char>> = Vec::new();
    for _ in 0..stack_map_tr[0].len() {
        stack_map.push(Vec::new())
    }
    for (_, line) in stack_map_tr.iter().enumerate() {
        for (j, c) in line.iter().enumerate() {
            if c != &' ' {
                stack_map[j].push(c);
            }
        }
    }

    // process the list of operations
    let re2 = Regex::new("move ([0-9]+) from ([0-99]+) to ([0-99]+)").unwrap();
    input_str_operations.trim().lines().for_each(|line| {
        let captures = re2.captures(line).unwrap();
        let qty = captures.get(1).unwrap().as_str().parse::<u64>().unwrap();
        let from = captures.get(2).unwrap().as_str().parse::<u64>().unwrap();
        let to = captures.get(3).unwrap().as_str().parse::<u64>().unwrap();
        for _ in 1..=qty {
            let crate_moved = stack_map[from as usize - 1].pop();
            stack_map[to as usize - 1].push(crate_moved.unwrap());
        }
    });

    let mut part1: String = "".to_string();
    for stack in stack_map {
        part1 += &*stack.last().unwrap().to_string();
    }
    println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 1 : {:?}", duration);

    // -------- Part 2 ---------
    let start = Instant::now();
    // let input_str = fs::read_to_string("src/input/ex05").unwrap();
    let input_str = fs::read_to_string("src/input/input05").unwrap();
    let re = Regex::new("\n\n|\r\n\r\n").unwrap();
    let mut split = re.split(&*input_str);
    let (input_str_stacks, input_str_operations): (&str, &str) =
        (split.next().unwrap(), split.next().unwrap());

    // process the stacks map
    let stack_map_tr = input_str_stacks
        .split_once(" 1")
        .unwrap()
        .0
        .lines()
        .rev()
        .map(|line| line.chars().skip(1).step_by(4).collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();
    // dbg!(&stack_map_tr);
    let mut stack_map: Vec<Vec<&char>> = Vec::new();
    for _ in 0..stack_map_tr[0].len() {
        stack_map.push(Vec::new())
    }
    for (_, line) in stack_map_tr.iter().enumerate() {
        for (j, c) in line.iter().enumerate() {
            if c != &' ' {
                stack_map[j].push(c);
            }
        }
    }

    // process the list of operations
    let re2 = Regex::new("move ([0-9]+) from ([0-99]+) to ([0-99]+)").unwrap();
    input_str_operations.trim().lines().for_each(|line| {
        let captures = re2.captures(line).unwrap();
        let qty = captures.get(1).unwrap().as_str().parse::<u64>().unwrap();
        let from = captures.get(2).unwrap().as_str().parse::<u64>().unwrap();
        let to = captures.get(3).unwrap().as_str().parse::<u64>().unwrap();
        let mut crates_being_handled = Vec::new();
        for _ in 1..=qty {
            crates_being_handled.insert(0, stack_map[from as usize - 1].pop().unwrap());
        }
        stack_map[to as usize - 1].append(&mut crates_being_handled);
    });

    let mut part2: String = "".to_string();
    for stack in stack_map {
        part2 += &*stack.last().unwrap().to_string();
    }
    println!("Part 2 : {part2}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 2 : {:?}", duration);
}
