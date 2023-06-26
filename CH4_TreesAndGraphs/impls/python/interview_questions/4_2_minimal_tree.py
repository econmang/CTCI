# Problem 4.2
# Given a sorted array with unique integer elements, write an algorithm to create a binary search tree with minimal height

from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, value: int, left: Optional[Node], right: Optional[Node]):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root: Optional[Node]):
        self.root = root

    def traverse(self, curr_node):
        if curr_node:
            print("root:",curr_node.value)
            if curr_node.left:
                print("left:", curr_node.left.value)
            if curr_node.right:
                print("right:", curr_node.right.value)
            self.traverse(curr_node.left)
            self.traverse(curr_node.right)
        else:
            print("None")

    @staticmethod
    def create_minimal_bst(sorted_list: list[int], start: int, end: int) -> Optional[Node]:
        if end < start:
            return None
        mid: int = (start + end) // 2
        n: Optional[Node] = Node(sorted_list[mid], BST.create_minimal_bst(sorted_list, start, mid - 1), BST.create_minimal_bst(sorted_list, mid + 1, end))
        return n

if __name__ == "__main__":
    sorted_list = [1,2,3,4,5,6,7,8,9,10]
    mid_node = BST.create_minimal_bst(sorted_list, 0, len(sorted_list) - 1)
    bst = BST(mid_node)
    bst.traverse(bst.root)
