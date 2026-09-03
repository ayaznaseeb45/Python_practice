class Stack:
    def __init__(self):
        self.stack = []

    # add elements 
    def push (self, data):
        self.stack.append(data)

    # remove element 
    def pop (self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return
        self.stack.pop()

    # peak check top element in stack 

    def peak (self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print(f"top element is '{self.stack[-1]}'.")

    # display stack elements 
    def display(self):
        if len(self.stack) == 0:
            print("No elements present")
            return
        print(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            print("empty")
            return
        else:
            result = len(self.stack)
            print(f"total elements present are {result} which are", end=" -> ")
            self.display()


s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.pop()
s.display()
s.peak()
s.is_empty()