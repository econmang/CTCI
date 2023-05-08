pub mod bs {
    use std::cmp::Ordering;

    pub fn binary_search(num_list: &Vec<i32>, item: i32) -> i32 {
        let mut low = 0;
        let mut high = num_list.len() - 1;

        while low <= high {
            let guess_idx = (high + low) / 2;
            let guess = num_list[guess_idx];

            match guess.cmp(&item) {
                Ordering::Less => { low = guess_idx + 1; },
                Ordering::Greater => { high = guess_idx - 1; },
                Ordering::Equal => { return guess_idx as i32 },
            }
        }
        return -1;
    }
}
