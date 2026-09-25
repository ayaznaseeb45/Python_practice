class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            print("Linked List is Not Empty")


ll = LinkedList()

ll.is_empty()

ll.head = Node(10)
ll.is_empty()