# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __setleft__(self, node):
        self.left = node

    def __setright__(self, node):
        self.right = node

    def __setparent__(self, node):
        self.parent = node

class BST:
    def __init__(self, root):
        self.root = root

    @staticmethod
    def leftmost_child(node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    @staticmethod
    def successor(node):
        if node.right:
            return BST.leftmost_child(node.right)
        else:
            parent = node.parent
            while parent and parent.left != node:
                node = parent
                parent = node.parent
            return parent

if __name__ == "__main__":
    # Set up successor test case
    node_d = Node('d')
    node_b = Node('b')
    node_f = Node('f')
    node_a = Node('a')
    node_c = Node('c')
    node_e = Node('e')
    node_g = Node('g')
    node_d.left = node_b
    node_d.right = node_f
    node_b.parent = node_d
    node_f.parent = node_d
    node_b.left = node_a
    node_b.right = node_c
    node_a.parent = node_b
    node_c.parent = node_b
    node_f.left = node_e
    node_f.right = node_g
    node_e.parent = node_f
    node_g.parent = node_f
    bst = BST(node_d)

    succ = BST.successor(bst.root)
    if succ:
        print("Found successor:" + succ.data)
    else:
        print("No successor found")
