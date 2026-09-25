class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, data):
        self.stack.append(data)

    # Pop
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        return self.stack.pop()

    # Peek
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return stack size
    def size(self):
        return len(self.stack)

    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print(self.stack)


# Driver Code
s = Stack()

# Push
s.push(10)
s.push(20)
s.push(30)

print("Stack:")
s.display()

# Peek
print("Top Element:", s.peek())

# Pop
print("Removed Element:", s.pop())

print("Stack After Pop:")
s.display()

# Size
print("Size:", s.size())

# Is Empty
print("Is Empty:", s.is_empty())