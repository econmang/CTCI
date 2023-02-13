use std::collections::HashSet;

fn is_unique(search_str: &str)-> bool {
    let mut search_set: HashSet<char> = HashSet::new();

    for c in search_str.chars() {
        search_set.insert(c);
    }

    let collect_str: _ = search_set.iter().collect::<Vec<&char>>().iter().collect::<String>();

    if search_str.len() == search_set.iter().collect::<Vec<&char>>().len() {
        return true;
    }
    return false;
}

fn main() {
    let search_str: String = "unique?".to_string();
    let unique_check: bool = is_unique(&search_str);

    println!("{unique_check}");
}
