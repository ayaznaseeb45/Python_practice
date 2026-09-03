class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    # Check if list is empty
    def is_empty(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            print("Linked List is not empty")

    # Traversal
    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Insert at beginning
    def insert_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Insert after middle node
    def insert_middle(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        slow = self.head
        fast = self.head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node.next = slow.next
        slow.next = new_node

    # Insert at specific position
    def insert_position(self, position, data):
        new_node = Node(data)

        # Insert at beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        # Move to previous node
        for i in range(position - 1):
            if current is None:
                print("Invalid Position")
                return
            current = current.next

        if current is None:
            print("Invalid Position")
            return

        # Insert node
        new_node.next = current.next
        current.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        # Move to second-last node
        while current.next.next is not None:
            current = current.next

        # Delete last node
        current.next = None


# -------------------------
# Testing
# -------------------------

ll = SinglyLL()

ll.insert_begining(30)
ll.insert_begining(20)
ll.insert_begining(10)

ll.insert_end(500)
ll.insert_middle(300)

print("Original:")
ll.traversal()

ll.delete_beginning()
print("\nAfter Delete Beginning:")
ll.traversal()

ll.delete_end()
print("\nAfter Delete End:")
ll.traversal()