class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def enQueue(self, element):
        self.queue.append(element)
        self.length += 1

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
            raise TypeError("Empty Queue")
        else:
            self.length -= 1
            return self.queue.pop(0)

    def getFront(self):
        if self.isEmpty():
            raise TypeError("Empty Queue")
        else:
            return self.queue[0]

    def getLast(self):
        if self.isEmpty():
            raise TypeError("Empty Queue")
        else:
            return self.queue[-1]

    def size(self):
        return self.length

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False


my_queue = Queue()
for i in range(0, 6):
    my_queue.enQueue(i)

print(my_queue.getFront())
print(my_queue.getLast())
print(my_queue.size())
