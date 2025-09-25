class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def insertNode(self, root, node):
        if root is None:
            return node
        else:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insertNode(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insertNode(root.right, node)
        return root

    def delNode(self, root, data):
        if root is None:
            return None

        if root.data == data:
            # Case 1 & 2: node with 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Case 3: node with 2 children
                [psucc, succ] = self.findMin(root.right, root)
                if psucc != root:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                succ.left = root.left
                succ.right = root.right
                return succ
        elif data < root.data:
            root.left = self.delNode(root.left, data)
        else:
            root.right = self.delNode(root.right, data)

        return root

    def findMin(self, root, parent):
        if root.left:
            return self.findMin(root.left, root)
        else:
            return [parent, root]


# ------------------ Driver Code ------------------

A = BSTNode(10)
B = BSTNode(6)
C = BSTNode(12)
D = BSTNode(2)
E = BSTNode(8)
F = BSTNode(13)

t1 = BSTree(A)
t1.insertNode(t1.root, B)
t1.insertNode(t1.root, C)
t1.insertNode(t1.root, D)
t1.insertNode(t1.root, E)
t1.insertNode(t1.root, F)

print("Initial Preorder Traversal:")
t1.preorder(t1.root)
print("\n")

# 1. Node with 0 child
# t1.root = t1.delNode(t1.root, 13)
# print("After deleting 13 (leaf):")
# t1.preorder(t1.root)
# print("\n")

# 2. Node with 1 child
# t1.root = t1.delNode(t1.root, 12)
# print("After deleting 12 (one child):")
# t1.preorder(t1.root)
# print("\n")

# 3. Node with 2 children
# t1.root = t1.delNode(t1.root, 10)
# print("After deleting 10 (two children):")
# t1.preorder(t1.root)
# print("\n")
