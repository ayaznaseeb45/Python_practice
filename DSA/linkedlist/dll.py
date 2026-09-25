class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next:
            current = current.next

        current.prev.next = None

    # Forward Traversal
    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


# Driver Code
dll = DoublyLL()

dll.insert_beginning(10)
dll.insert_beginning(20)
dll.insert_beginning(30)
dll.insert_end(50000)

dll.traversal()

# dll.delete_beginning()
# dll.delete_end()
# dll.traversal()