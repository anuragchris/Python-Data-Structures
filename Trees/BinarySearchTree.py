class BST:

    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self is None:
            return False

        if self.key == data:
            return True

        if self.key < data:
            if self.right is not None:
                return self.right.search(data)
            return False

        else:
            if self.right is not None:
                return self.left.search(data)
            return False

    def preOrder(self):
        if self is None:
            return None
        print(self.key)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.preOrder()
        print(self.key)
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.key)

    def delete(self, data):
        if not self.key:
            print("Tree is Empty")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Given Node is not present in the Tree")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Give node is not present in the Tree")
        else:
            if not self.left:
                temp = self.right
                self = None
                return temp
            if not self.right:
                temp = self.left
                self = None
                return temp
            node = self.right
            while self.left:
                node = self.left
                self.key = node.key
                self.right = self.right.delete(node.key)
            return self

    def count(self):
        if not self:
            return 0
        if not self.left and not self.right:
            return 1
        elif not self.left and self.right:
            return 1+self.right.count()
        elif not self.right and self.left:
            return 1+self.left.count()
        else:
            return 1+self.left.count()+self.right.count()

    def min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def max(self):
        currrent = self
        while currrent.right:
            currrent = currrent.right
        return currrent


root = BST(None)
root.insert(10)
print(root.key)
root.insert(30)
root.insert(5)
print(root.right.key)
print(root.search(40))
# root.preOrder()
# root.inOrder()
root.delete(30)
root.postOrder()
print(root.count())
