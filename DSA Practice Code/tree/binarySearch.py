class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


# Create Tree
root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(2)
root.left.right = Node(8)


# Mirror Function rotate to 180 degree 

def mirror(root):
    if root is None:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)

    return root


mirror(root)