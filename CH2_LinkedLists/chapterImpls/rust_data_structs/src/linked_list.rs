pub struct Node {
    pub prev: Option<Box<Node>>,
    pub next: Option<Box<Node>>,
    pub value: i32
}

impl Node {
    pub fn get_value(&self) -> i32 {
        self.value
    }

    pub fn get_next(&self) -> &Option<Box<Node>> {
        &self.next
    }
    
    pub fn get_prev(&self) -> &Option<Box<Node>> {
        &self.prev
    }
}

pub struct LinkedList {
    pub head: Box<Node>
}

impl LinkedList {
    pub fn get_head(&self) -> &Box<Node> {
        &self.head
    }
    
    pub fn traverse(&self) -> Option<Box<Node>> {
        let head = self.get_head();
        let mut curr = &head.next;
        
        while curr.as_ref().is_some() {
            curr = &curr.as_ref().unwrap().next;
        }
    }

    
}
