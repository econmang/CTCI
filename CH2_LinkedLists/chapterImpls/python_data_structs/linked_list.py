class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self, head):
        self.head = head

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_dupes(self):
        existing_data = {}
        current_node = self.head
        while current_node:
            if current_node.data in existing_data and current_node.prev:
                current_node.prev.set_next(current_node.next)
                try:
                    current_node.next.set_prev(current_node.prev)
                except:
                    current_node.next = None
                current_node = current_node.next
            else:
                existing_data[current_node.data] = True
                current_node = current_node.next

    def kth_from_last(self, k):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        for _ in range(k):
            current_node = current_node.prev if current_node else None
        return current_node.data if current_node else None

    def gen_dupe_test(self):
        self.head = Node(1)
        node2 = Node(3)
        node3 = Node(3)
        node4 = Node(3)
        self.head.set_next(node2)
        node2.set_next(node3)
        node2.set_prev(self.head)
        node3.set_next(node4)
        node3.set_prev(node2)
        node4.set_prev(node3)

    def gen_kth_from_last_test(self):
        self.head = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        self.head.set_next(node2)
        node2.set_next(node3)
        node2.set_prev(self.head)
        node3.set_next(node4)
        node3.set_prev(node2)
        node4.set_prev(node3)

    def deleteNode(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                current_node.prev.set_next(current_node.next if current_node else None)
                current_node.next.set_prev(current_node.prev if current_node else None)
                current_node = None
            else:
                current_node = current_node.next
    
    def sum_lists(self, second_list_head: Node):
        curr_node_1 = self.head
        curr_node_2 = second_list_head
        sum_list_1 = 0
        sum_list_2 = 0
        while curr_node_1:
            sum_list_1 += curr_node_1.data
            curr_node_1 = curr_node_1.next
        while curr_node_2:
            sum_list_2 += curr_node_2.data
            curr_node_2 = curr_node_2.next
        return sum_list_1 + sum_list_2

if __name__ == '__main__':
    # Create a linked list with 3 nodes
    node1 = Node(1)
    linked_list = LinkedList(node1)
    linked_list.gen_dupe_test()
    print("Initial list")
    linked_list.traverse()
    print("Removing duplicates")
    linked_list.remove_dupes()
    linked_list.traverse()
    print("Kth from last")
    linked_list.gen_kth_from_last_test()
    print(linked_list.kth_from_last(2))
    print("Deleting node")
    linked_list.deleteNode(3)
    linked_list.traverse()
