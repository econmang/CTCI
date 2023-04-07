use stacks_and_queues::stacks::Stack;

fn main() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.push(5);
    println!("stack: {:?}", stack.stack);
    println!("peek: {:?}", stack.peek());
    println!("pop: {:?}", stack.pop());
    println!("stack: {:?}", stack.stack);
    println!("is_empty: {:?}", stack.is_empty());
    println!("pop: {:?}", stack.pop());
}
