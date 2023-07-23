# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.visited = False

