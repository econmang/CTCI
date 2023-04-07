use stacks_and_queues::stacks::Stack;
use stacks_and_queues::queues::Queue;

fn main() {
    println!("Stack Example:");
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

    println!("\nQueue Example:");
    let mut queue = Queue::new();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);
    println!("queue: {:?}", queue.queue);
    queue.enqueue(6);
    println!("enqueued 6: {:?}", queue.queue);
    println!("dequeue: {:?}", queue.dequeue());
}
