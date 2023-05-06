use rand::Rng;
use binary_search::bs::binary_search;

fn main() {
    let mut num_list: Vec<i32> = Vec::new();

    let mut item: i32 = -1;
    for i in 0..100000 {
        let num: i32 = rand::thread_rng().gen_range(0..100000);
        if i == 77 {
            item = num;
        }
        num_list.push(num);
    }
    num_list.sort();

    println!("Missing search idx:");
    println!("{}",binary_search(&num_list, 100001));

    println!("Found search idx:");
    println!("{}",binary_search(&num_list, item));

    println!("Missing search idx:");
    println!("{}",binary_search(&num_list, -100));

}
