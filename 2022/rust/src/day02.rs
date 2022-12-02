use std::error::Error;
use std::fs;


fn main() -> Result<(), Box<dyn Error>> {

    // -------- Part 1 ---------
    let input = fs::read_to_string("input/input02")?;
    let input = input.trim();
    dbg!(&input);
    Ok(())
}
