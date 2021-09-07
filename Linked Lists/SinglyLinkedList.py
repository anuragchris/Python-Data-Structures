from typing import Type


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_Node

    def addFirst(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def addLast(self, data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_Node

    def insertAfter(self, index, data):
        if index < 0:
            raise IndexError(("Invalid Index"))

        elif index == 0:
            new_Node = Node(data)
            if not self.head:
                self.head = new_Node
            else:
                new_Node.next = self.head
                self.head = new_Node

        else:
            if not self.head:
                raise IndexError(
                    "Empty Linked List. Cannot Enter a new Node at index other than 0.")
            else:
                new_Node = Node(data)
                length = 0
                n = self.head
                check = False
                while n.next is not None:
                    n = n.next
                    length += 1
                    if length == index:
                        new_Node.next = n.next
                        n.next = new_Node
                        check = True
                        break
                if not check:
                    raise IndexError(
                        "Invalid Index. Index greater than Length of Linked List.")

    def insertBefore(self, index, data):
        if index <= 0:
            raise TypeError(
                "Invalid Index. Index cannot be less than or equal to 0")
        else:
            n = self.head
            length = 0
            check = False
            while n.next is not None:
                if (index-1 == length):
                    new_Node = Node(data)
                    new_Node.next = n.next
                    n.next = new_Node
                    check = True
                    break
                n = n.next
                length += 1
            if not check:
                raise IndexError(
                    "Invalid Index. Index greater than length of Linked List")

    def removeFirst(self):
        if self.head is None:
            raise TypeError("Empty Linked List")
        else:
            temp = self.head
            self.head = self.head.next
            temp = None

    def removeLast(self):
        if self.head is None:
            raise TypeError("Empty Linked List")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while(temp.next.next):
                temp = temp.next
            temp.next = None

    def remove(self, index):
        if self.head is None:
            raise TypeError("Empty Linked List")
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
        elif index < 0:
            raise IndexError("Invalid Index")
        else:
            length = 0
            check = False
            temp = self.head
            while temp.next is not None:
                length += 1
                if (length == index):
                    temp2 = temp.next
                    temp.next = temp2.next
                    temp2 = None
                    check = True
                    break
                else:
                    temp = temp.next
            if not check:
                raise IndexError("Index is greater than length of Linked List")

    def traverse(self):
        if not self.head:
            raise TypeError("Empty Linked List")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next


ll = LinkedList()
ll.addFirst(10)
ll.addFirst(20)
ll.addLast(30)
ll.insertAfter(1, 40)
ll.insertBefore(1, 50)
ll.add(100)
ll.removeFirst()
ll.removeLast()
ll.remove(2)
ll.traverse()
