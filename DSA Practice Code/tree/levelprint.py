from collections import deque


# Node of BST
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert into BST
def insert(root, data):

    # If tree is empty, create first node
    if root is None:
        return Node(data)

    # Go to left subtree
    if data < root.data:
        root.left = insert(root.left, data)

    # Go to right subtree
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# -----------------------
# Create BST
# -----------------------

root = None

numbers = [50, 30, 70, 20, 40, 60, 80]

for num in numbers:
    root = insert(root, num)