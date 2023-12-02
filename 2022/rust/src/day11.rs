use std::fs;
use std::time::Instant;

enum Operation {
    Add(u64),
    Mul(u64),
    Sqr,
}

struct Monkey {
    items: Vec<u64>,
    operation: Operation,
    test_div_by: u64,
    throw_to_if_true: u8,
    throw_to_if_false: u8,
}

impl Monkey {
    fn do_operation(&self, worry_level: u64) -> u64 {
        match self.operation {
            Operation::Add(n) => worry_level + n,
            Operation::Mul(n) => worry_level * n,
            Operation::Sqr => worry_level * worry_level,
        }
    }

    fn yeet(&self, worry_level: u64) -> u8 {
        if worry_level % self.test_div_by == 0 {
            self.throw_to_if_true
        } else {
            self.throw_to_if_false
        }
    }
}


fn main() {
    println!("Advent of Code 2022 - Jour 11");

    // -------- Part 1 ---------
    let start = Instant::now();
    let input_str = fs::read_to_string("src/input/ex11").unwrap();
    // let input_str = fs::read_to_string("src/input/input11").unwrap();
    let input_str = input_str.trim();
    let monkey_list = input_str.split("\n\n").map(|monkey_str| {
        let mut lines = monkey_str.lines();
        lines.next();
        Monkey{items: lines.next().unwrap()[17..].split(", ").map(|n| n.parse().unwrap()).collect(),
        operation:lines.next().unwrap()
        }
}

    )



    // println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 1 : {:?}", duration);

    // -------- Part 2 ---------
    let start = Instant::now();
    let input_str = fs::read_to_string("src/input/ex11").unwrap();
    // let input_str = fs::read_to_string("src/input/input11").unwrap();
    let input_str = input_str.trim();

    // println!("Part 2 : {part2}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 2 : {:?}", duration);
}
