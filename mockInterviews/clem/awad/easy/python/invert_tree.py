class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setleft(self, left):
        self.left = left
    def setright(self, right):
        self.right = right

class BT:
    def __init__(self, root):
        self.root = root

    @staticmethod
    def invert(root):
        if root is None:
            pass
        else:
            BT.invert(root.left)
            BT.invert(root.right)
            save = root.left
            root.left = root.right
            root.right = save

    def traverse(self, node, lvl):
        if node:
            print(lvl, ": ",node.val)
            self.traverse(node.left, lvl + 1)
            self.traverse(node.right, lvl + 1)


if __name__ == "__main__":
    a = Node(4)
    b = Node(2)
    c = Node(1)
    d = Node(3)
    e = Node(7)
    f = Node(6)
    g = Node(9)

    a.left = b
    b.left = c
    b.right = d
    a.right = e
    e.left = f
    e.right = g
    
    bt = BT(a)
    
    bt.traverse(bt.root, 1);
    BT.invert(bt.root)
    print("\nInverting\n")
    bt.traverse(bt.root, 1);
