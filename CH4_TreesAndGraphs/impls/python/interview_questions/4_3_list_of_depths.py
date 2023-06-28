# Problem 4.3
# Given a binary tree, design an algorithm which creates a linked list of all nodes
# at each depth (e.g. if you have a with depth, D, you'll have D linked lists).

from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, value: int, left: Optional[TreeNode], right: Optional[TreeNode]):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root

class LLNode:
    def __init__(self, value: int, prev: Optional[LLNode], next: Optional[LLNode]):
        self.value = value
        self.prev = prev
        self.next = next
class LL:
    def __init__(self, head: LLNode):
        self.head = head

    def insert(self, next: LLNode):
        currNode = self.head
        while(currNode.next):
            currNode = currNode.next
        currNode.next = next
        currNode.next.prev = currNode

    def traverse(self):
        currNode = self.head
        ll_str = ""
        while currNode:
            ll_str += str(currNode.value) + " > "
            currNode = currNode.next
        return ll_str

    @staticmethod
    def traverse_bt(root: Optional[TreeNode], lists: dict, level: int):
        if root:
            LL.traverse_bt(root.left, lists, level + 1)
            LL.traverse_bt(root.right, lists, level + 1)
            if level in lists.keys():
                lists[level].insert(LLNode(root.value, None, None))
            else:
                lists[level] = LL(LLNode(root.value, None, None))

if __name__ == "__main__":
    # Initialize dict that will be used to hold the head nodes of each
    # Note: Each index indicates the depth
    depth_lists = {}

    l2leaf: TreeNode = TreeNode(4, None, None)
    r2leaf: TreeNode = TreeNode(5, None, None)
    l3leaf: TreeNode = TreeNode(6, None, None)
    lleaf: TreeNode = TreeNode(1, l2leaf, r2leaf)
    rleaf: TreeNode = TreeNode(3, l3leaf, None)
    root: TreeNode = TreeNode(2, None, None)
    root.left = lleaf
    root.right = rleaf

    bt: BinaryTree = BinaryTree(root)
    LL.traverse_bt(bt.root, depth_lists, 0)
    for key in depth_lists.keys():
        print("Level: ",key)
        print(depth_lists[key].traverse())
