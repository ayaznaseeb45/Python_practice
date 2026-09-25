class Queue:
    def __init__(self):
        self.queue = []


    # Enqueue add element at the end 
    def enqueue(self, data):
        self.queue.append(data)

    # dequeue remove element from top

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        self.queue.pop(0)


    # show data in queue 
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        print(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()