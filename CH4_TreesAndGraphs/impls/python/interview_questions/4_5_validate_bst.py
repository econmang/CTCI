class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

class BST:
    def __init__(self, root):
        self.root = root

    @staticmethod
    def validate_bst(tree):
        if tree is None:
            return True
        if tree.left:
            if tree.left.val >= tree.val:
                return False
        if tree.right:
            if tree.right.val <= tree.val:
                return False
        return BST.validate_bst(tree.left) and BST.validate_bst(tree.right)

if __name__ == "__main__":
    #[5,4,6,null,null,3,7]
    #       (5)
    #      /   \
    #    (4)   (6)
    #          / \
    #        (3) (7)

    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(6)
    # tree.left.left = TreeNode(1)
    # tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(7)

    isValid = BST.validate_bst(tree)
    print(isValid)
    assert isValid == False
