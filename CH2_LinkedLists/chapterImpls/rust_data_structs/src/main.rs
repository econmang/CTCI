use rust_data_structs::linked_list::{self, UnidirectionalNode, SinglyLinkedList};

fn main() {
    let uni_node: UnidirectionalNode = UnidirectionalNode { next: None, value: 3 };
    let sll: SinglyLinkedList = SinglyLinkedList { head: &uni_node };
}
