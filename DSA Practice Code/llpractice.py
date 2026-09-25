# practice for singli linklist 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class S_linklist:
    def __init__(self):
        self.head = None

        # check if list is empty 
        def is_empty(self):
            if self.head is None:
                print("Linklist is empty")
            else:
                print("Linklist is Not empty")

        # check traversal code 
        def traversal(self):
            if self.head is None:
                print("Linklist is empty")
                return

            current = self.head

            while current != None:
                print(current.data, end= " -> ")
                current = current.next

            print("None")

        # insertion at begining 
        def insert_begining(self, data):
            new_node = Node(data)

            new_node.next = self.head
            self.head = new_node

        # insertion at the end 
        def insert_end(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            current = self.head

            while current.next:
                current = current.next 

            current.next = new_node

        # insert at middle node 
        def insert_mid (self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            slow = self.head
            fast = self.head

            while fast.next is not None and fast.next.next is not None:
                slow = slow.next 
                fast = fast.next.next 

            new_node = slow.next 
            slow.next = new_node

        # delete from  beginning 

        def delte_beginning(self):
            if self.head is None:
                print("LL is already empty")
                return
            self.head = self.head.next 

        # delete from end
        def delte_end(self):
            if self.head is None:
                print("Link list is empty")
                return

            # only one node 
            if self.head.next is None:
                self.head = None
                return

            current = self.head

            while current.next.next is not None:
                current = current.next 

            # delte last node 
            current.next = None
                



                



