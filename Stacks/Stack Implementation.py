class Stack:
    stack = []
    current_size = 0

    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.current_size

    def push(self, element):
        if self.getSize() > self.size:
            return OverflowError
        else:
            self.stack.append(element)
            self.current_size += 1
            return True

    def pop(self):
        if self.getSize() == 0:
            print("Stack UnderFlow")
            return -1
        else:
            self.current_size -= 1
            return self.stack.pop

    def peek(self):
        if self.getSize() == 0:
            return "Empty Stack"
        else:
            return self.stack[self.current_size-1]


my_stack = Stack(10)
my_stack.pop()
my_stack.push(20)
print(my_stack.peek())
print(my_stack.peek())
