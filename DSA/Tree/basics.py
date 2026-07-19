class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    # Set root
    def set_root(self, val):
        self.root = Node(val)

    # Insert left child
    def insert_left(self, parent, val):
        if parent is None:
            return
        parent.left = Node(val)

    # Insert right child
    def insert_right(self, parent, val):
        if parent is None:
            return
        parent.right = Node(val)

    # Preorder Traversal
    def preorder(self, root):
        if root is None:
            return

        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # Inorder Traversal
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")


tree = Tree()
tree.set_root(1)

tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)

tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

tree.insert_left(tree.root.right, 6)
tree.insert_right(tree.root.right, 7)

print("Preorder:")
tree.preorder(tree.root)

print("\nInorder:")
tree.inorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)