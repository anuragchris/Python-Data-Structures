class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def addFirst(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            new_node = Node(data)
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node

    def addLast(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        elif self.head.next is None:
            new_node = Node(data)
            self.head.next = new_node
            new_node.prev = self.head

        else:
            temp = self.head
            new_node = Node(data)
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Invalid Index")

        elif index == 0:
            if self.head is None:
                new_node = Node(data)
                self.head = new_node
            else:
                new_node = Node(data)
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node

        else:
            length = 0
            check = False
            temp = self.head

            while temp.next is not None:
                length += 1
                if(length == index):
                    new_node = Node(data)
                    temp2 = temp.next
                    temp.next = new_node
                    new_node.next = temp2
                    temp2.prev = new_node
                    check = True
                    break
                temp = temp.next

            if index-length == 1:
                new_node = Node(data)
                temp.next = new_node
                new_node.prev = temp
                check = True

            if not check:
                raise IndexError(
                    "Invalid Index. Index greater than length of Linked List")

    def removeFirst(self):
        if not self.head:
            raise TypeError("Empty Linked List")

        elif self.head.next is None:
            self.head = None

        else:
            temp = self.head.next
            temp.prev = None
            self.head = None
            self.head = temp

    def removeLast(self):
        if self.head is None:
            raise TypeError("Empty Linked List")

        elif self.head.next is None:
            self.head = None

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp2 = temp.prev
            temp2.next = None
            temp = None

    def traverse(self):
        if not self.head:
            raise TypeError("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "<-->", end=" ")
                temp = temp.next


dll = DoublyLinkedList()
dll.addFirst(20)
dll.addFirst(30)
dll.addLast(40)
dll.insert(3, 100)
dll.removeFirst()
dll.removeLast()
dll.addLast(100)
dll.addFirst(200)
dll.insert(2, 300)
dll.removeFirst()
dll.removeLast()
dll.traverse()
