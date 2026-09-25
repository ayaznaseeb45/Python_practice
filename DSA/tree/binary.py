from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # preorder DFs
    def preorder(root):
        if root is None:
            return

        print(root.data, end=" <-> ")

        Node.preorder(root.left)
        Node.preorder(root.right)

    # inorder 
    def inOrder(root):
        if root is None:
            return

        Node.inOrder(root.left)

        print(root.data, end=" ")

        Node.inOrder(root.right)

    def postorder(root):
        if None is None:
            return

        Node.postorder(root.left)
        Node.postorder(root.right)
        print(root.data, end="")


    def level(root):
        if root is None:
            return

        queue = deque()

        queue.append(root)

        while queue :
            current = queue.popleft()

            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)



root = Node(15)
root.left = Node(5)
root.right = Node(10)

root.left.left = Node(3)
root.left.right = Node(2)

root.right.left = Node(7)
root.right.right = Node(4)

Node.preorder(root)

Node.inOrder(root)

Node.inOrder(root)

# print(root.data)
# print(root.left.data)
# print(root.right.data)

# print(root.left.left.data)
# print(root.left.right.data)

# print(root.right.left.data)
# print(root.right.right.data)
