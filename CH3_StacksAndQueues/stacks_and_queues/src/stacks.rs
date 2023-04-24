pub struct Stack<T> {
    pub stack: Vec<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Self { stack: Vec::new() }
    }

    pub fn push(&mut self, item: T) {
        self.stack.push(item);
    }

    pub fn pop(&mut self) -> Option<T> {
        self.stack.pop()
    }

    pub fn peek(&self) -> Option<&T> {
        self.stack.last()
    }

    pub fn is_empty(&self) -> bool {
        self.stack.is_empty()
    }
}

#[cfg(test)]
mod tests {
    //use super::*;

    // There would ostensibly be array equivalents for the array stack implementations
    // push would migrate existing items in the array from a given stack's starting point up to the
    // stack capacity, pop would do something similar in the reverse direction, etc.
    // I am being lazy
    // fn three_stacks_one_array () {
    //     let mut array: [Option<i32>; 9]  = [None; 9];
    //     let stack_capacity = 3;
    //     
    //     let mut stack1 = Stack::new();
    //     stack1.push(1);
    //     stack1.push(2);
    //     stack1.push(3);
    //     let mut stack2 = Stack::new();
    //     stack2.push(4);
    //     stack2.push(5);
    //     stack2.push(6);
    //     let mut stack3 = Stack::new();
    //     stack3.push(7);
    //     stack3.push(8);
    //     stack3.push(9);
    //
    // }
}
