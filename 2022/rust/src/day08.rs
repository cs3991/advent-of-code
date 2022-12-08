use std::fs;
use std::time::Instant;

fn main() {
    println!("Advent of Code 2022 - Jour 08");

    let start = Instant::now();

    let input_str = fs::read_to_string("src/input/input08").unwrap();
    let input_str = input_str.trim();
    let forest: Vec<Vec<u32>> = input_str
        .lines()
        .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect();

    // -------- Part 1 ---------
    // let input_str = fs::read_to_string("src/input/ex08").unwrap();
    let n = forest.len(); // we assume the forest has equal width and height
    let mut mask = vec![vec![' '; n]; n];
    let mut part1 = 0;
    for (i, line) in forest.iter().enumerate() {
        'tree_loop: for (j, &tree_height) in line.iter().enumerate() {
            // left to right
            let mut s = j;
            loop {
                if s == n - 1 {
                    part1 += 1;
                    mask[i][j] = '#';
                    continue 'tree_loop;
                }
                s += 1;
                if line[s] >= tree_height {
                    break;
                }
            }
            // right to left
            let mut s = j;
            loop {
                if s == 0 {
                    part1 += 1;
                    mask[i][j] = '#';
                    continue 'tree_loop;
                }
                s -= 1;
                if line[s] >= tree_height {
                    break;
                }
            }
            // top to down
            let mut s = i;
            loop {
                if s == n - 1 {
                    part1 += 1;
                    mask[i][j] = '#';
                    continue 'tree_loop;
                }
                s += 1;
                if forest[s][j] >= tree_height {
                    break;
                }
            }
            // down to top
            let mut s = i;
            loop {
                if s == 0 {
                    part1 += 1;
                    mask[i][j] = '#';
                    continue 'tree_loop;
                }
                s -= 1;
                if forest[s][j] >= tree_height {
                    break;
                }
            }
        }
    }

    println!("Part 1 : {part1}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 1 : {:?}", duration);

    // -------- Part 2 ---------
    let start = Instant::now();

    let n = forest.len(); // we assume the forest has equal width and height
    let mut part2 = 0;
    for (i, line) in forest.iter().enumerate() {
        for (j, &tree_height) in line.iter().enumerate() {
            let mut score: u64 = 1;

            // right
            let mut count = 0;
            for s in j + 1..n {
                count += 1;
                if forest[i][s] >= tree_height {
                    break;
                }
            }
            score *= count;
            // left
            let mut count = 0;
            for s in (0..j).rev() {
                count += 1;
                if forest[i][s] >= tree_height {
                    break;
                }
            }
            score *= count;
            // down
            let mut count = 0;
            for s in i + 1..n {
                count += 1;
                if forest[s][j] >= tree_height {
                    break;
                }
            }
            score *= count;
            // top
            let mut count = 0;
            for s in (0..i).rev() {
                count += 1;
                if forest[s][j] >= tree_height {
                    break;
                }
            }
            score *= count;
            if score > part2 {
                part2 = score;
            }
        }
    }

    println!("Part 2 : {part2}");

    let duration = start.elapsed();
    println!("Temps d'exécution de la partie 2 : {:?}", duration);
}
