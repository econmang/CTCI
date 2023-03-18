class UnidirectionalNode:
    def __init__(self, next, value):
        self.next = next
        self.value = value

    def get_next(self):
        return self.next
    def get_value(self):
        return self.value

    def set_next(self, next):
        self.next = next
    def set_value(self, value):
        self.value = value

class SinglyLinkedList:
    def __init__(self, head: UnidirectionalNode):
        self.head = head

    def get_head(self):
        return self.head
    def set_head(self, head: UnidirectionalNode):
        self.head = head

    def traverse(self):
        curr = self.get_head()
        while curr.next != None:
            curr = curr.next
        return curr

    def append_to_tail(self, value):
        final_node = self.traverse()
        new_node: UnidirectionalNode = UnidirectionalNode(None, value)
        final_node.next = new_node

    def search(self, value):
        curr = self.get_head()
        while (curr != None):
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def delete(self, value):
        curr = self.get_head()
        if curr == None:
            return None
        elif curr.value == value:
            self.set_head(curr.next)
            return self.get_head()
        while curr.get_next() != None:
            if curr.get_next().get_value() == value:
                curr.set_next(curr.get_next().get_next())
                return self.get_head()
        return self.get_head()
