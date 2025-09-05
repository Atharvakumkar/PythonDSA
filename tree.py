class BSNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BSTree:
    def __init__(self):
        self.root = None  # Initialize root of the BST as None

    def insertNode(self, root, node):
        if root is None:
            return node
        else:
            if node.data < root.data:
                root.left = self.insertNode(root.left, node)
            else:
                root.right = self.insertNode(root.right, node)
        return root

    def insertNode(self, data):
        new_node = BSNode(data)
        if self.root is None:
            self.root = new_node
        else:
            self.root = self.insertNode(self.root, new_node)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=' ')

    def preOrder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.data, end=' ')
            self.inOrder(node.right)
