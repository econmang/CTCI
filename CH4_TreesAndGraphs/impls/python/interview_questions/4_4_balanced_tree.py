# Problem 4.4
# Given a binary tree, design an algorithm that determines if it is balanced.
# This means that the absolute difference of the heights of the left and right are less than or equal to 1.

def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

def is_balanced(root):
    if root is None:
        return True
    return abs(height(root.left) - height(root.right)) <= 1
