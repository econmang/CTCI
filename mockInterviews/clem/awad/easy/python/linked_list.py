from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def append(self, new_node: Node):
        current: Optional[Node] = self.head

        while current != None and current.next != None:
            current = current.next
        if current != None:
            current.next = new_node

    def reverse(self):
        current = self.head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linked_list = LinkedList(node1)
    linked_list.append(node2)
    linked_list.append(node3)

    linked_list.reverse()
    assert linked_list.head.data == 3
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 1
    assert linked_list.head.next.next.next == None
    print('Ok')
