pub struct Node {
    pub prev: Option<Box<Node>>,
    pub next: Option<Box<Node>>,
    pub value: i32
}

pub struct LinkedList {
    pub head: Option<Box<Node>>
}

impl LinkedList {
    fn traverse(&self) -> Option<Box<Node>> {
        let mut curr_node = &self.head;
        if curr_node.is_none() {
            return None;
        }

        let a = curr_node.unwrap();

        let n = Node {
            prev: None,
            next: None,
            value: 32
        };
        Some(Box::new(n))
    }
}
