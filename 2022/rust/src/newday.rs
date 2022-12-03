use dotenv;
use reqwest::blocking::Client;
use std::env;
use std::fs::File;
use std::io;
use std::io::{Read, Write};
use std::path::Path;

fn main() {
    let day: u64;
    loop {
        let mut day_str = String::new();
        println!("Which day do you want to generate?");
        io::stdin()
            .read_line(&mut day_str)
            .expect("Failed to read line");
        day = match day_str.trim().parse() {
            // Tentative de parse, si c'est un nombre, on sort de la boucle
            Ok(num) => match num {
                // On veut un nombre entre 1 et 25
                1..=25 => num,
                _ => {
                    println!("Please enter a number between 1 and 25");
                    continue;
                }
            },
            // Si ce n'est pas un nombre, on recommence
            Err(_) => {
                println!("Please type a number!");
                continue;
            }
        };
        break;
    }
    println!("Day {}", day);

    // verify if the file corresponding to that day exists
    let path = format!("src/day{:02}.rs", day);
    if Path::new(&path).exists() {
        println!("The file {} already exists", path);
        return;
    }
    let mut file = File::create(path).expect("Unable to create file");
    // get the content of the template file, replace the day number and write it to the new file
    let template = include_str!("template.rs");
    let content = template.replace("XX", format!("{:02}", day).as_str());
    file.write_all(content.as_bytes())
        .expect("Unable to write template code to new file");

    // download the input file from https://adventofcode.com/2022/day/{day}/input
    dotenv::from_filename("src/.env").expect("Unable to load .env file");
    let aoc_session = env::var("AOC_SESSION").expect("AOC_SESSION environment variable not set");
    let user_agent = env::var("USER_AGENT").expect("USER_AGENT environment variable not set");
    let client = Client::new();
    let input = client
        .get(format!("https://adventofcode.com/2022/day/{}/input", day).as_str())
        .header("Cookie", "session=".to_owned() + &aoc_session)
        .header("User-Agent", user_agent);
    let input = input.send().expect("Unable to download input file");
    let input = input.text().expect("Unable to read input file");
    let mut file =
        File::create(format!("src/input/input{:02}", day)).expect("Unable to create input file");
    file.write_all(input.as_bytes())
        .expect("Unable to write input file");

    // create an example input file
    File::create(format!("src/input/ex{:02}", day))
        .expect("Unable to create example input file");

    // update the Cargo.toml file
    let mut cargo_toml = File::open("Cargo.toml").expect("Unable to open Cargo.toml file");
    let mut cargo_toml_content = String::new();
    cargo_toml
        .read_to_string(&mut cargo_toml_content)
        .expect("Unable to read Cargo.toml file");
    cargo_toml_content += format!("\n\n[[bin]]\nname = \"day{:02}\"\npath = \"src/day{:02}.rs\"", day, day).as_str();
    let mut cargo_toml = File::create("Cargo.toml").expect("Unable to open Cargo.toml file");
    cargo_toml
        .write_all(cargo_toml_content.as_bytes())
        .expect("Unable to write to Cargo.toml file");


    // create the run configuration for Clion from day01.xml
    let mut run_config = File::create(format!(".idea/runConfigurations/Day{:02}.xml", day)).expect("Unable to create run configuration file");
    let run_config_template = include_str!("../.idea/runConfigurations/day01.xml");
    let run_config_content = run_config_template.replace("01", format!("{:02}", day).as_str());
    run_config.write_all(run_config_content.as_bytes()).expect("Unable to write run configuration file");


    // open the new file in Clion
    std::process::Command::new("C:/Users/simar/AppData/Local/JetBrains/Toolbox/apps/CLion/ch-0/222.3739.54/bin/clion64.exe")
        .arg(format!("src/day{:02}.rs", day))
        .spawn()
        .expect("Unable to open file in Clion");

    // add the new files to git
    std::process::Command::new("git")
        .arg("add")
        .arg(format!("src/day{:02}.rs", day))
        .arg(format!("src/input/input{:02}", day))
        .arg(format!("src/input/ex{:02}", day))
        .spawn()
        .expect("Unable to add files to git");
}
