import math
import sys


class Heap:

    heap = []

    def __init__(self) -> None:
        self.heap = []

    def size(self) -> int:

        return len(self.heap)

    def __get_Parent(self, i: int) -> int:

        if i <= 0 or i > len(self.heap)-1:
            return -1

        parent = math.floor((i-1)/2)
        return parent

    def __getLeftChild(self, i: int) -> int:

        if i < 0 or i > len(self.heap)-1:
            return -1

        left = math.floor((2*i)+1)

        if left > len(self.heap)-1 or left < 0:
            return -1

        return left

    def __getRightChild(self, i: int) -> int:

        right = math.floor((2*i)+2)

        if i < 0 or i > len(self.heap)-1 or right > len(self.heap)-1:
            return -1

        return right

    def __percolateDown(self, i: int):

        left = self.__getLeftChild(i)
        right = self.__getRightChild(i)
        min: int

        if left != -1 and self.heap[left] < self.heap[i]:
            min = left

        else:
            min = i

        if right != -1 and self.heap[right] < self.heap[min]:
            min = right

        if min != i:
            temp: int = self.heap[i]
            self.heap[i] = self.heap[min]
            self.heap[min] = temp
            self.__percolateDown(min)

    def push(self, data: int):

        self.heap.append(data)
        current: int = len(self.heap)-1

        while(current != 0 and self.heap[self.__get_Parent(current)] > self.heap[current]):

            temp = self.heap[math.floor((current-1)/2)]
            self.heap[math.floor((current-1)/2)] = self.heap[current]
            self.heap[current] = temp

            current = self.__get_Parent(current)

    def __decrease_key(self, index: int, val: int):

        self.heap[index] = val

        while(index != 0 and self.heap[self.__get_Parent(index)] > self.heap[index]):
            temp = self.heap[index]
            self.heap[index] = self.heap[math.floor((index-1)/2)]
            self.heap[math.floor((index-1)/2)] = temp

            index = math.floor((index-1)/2)

    def __increase_key(self, index: int, val: int):
        self.heap[index] = val
        self.__percolateDown(index)

    def change_key(self, index: int, val: int):
        if index > len(self.heap)-1:
            raise IndexError(
                f"Invalid Index: {index} For Heap Size: {len(self.heap)}")

        prev: int = self.heap[index]

        if prev > val:
            self.__decrease_key(index, val)
        else:
            self.__increase_key(index, val)

    def delete_min(self) -> int:

        if len(self.heap) == 0:
            raise IndexError("Empty Heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        root: int = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__percolateDown(0)
        return root

    def delete_key(self, index: int):
        value = self.heap[index]

        self.__decrease_key(index, -(sys.maxsize)-1)
        self.delete_min()

        return value

    def display_Heap(self):
        print(self.heap)


heap = Heap()
# heap.push(1000)
# heap.push(10000)
# heap.push(20)
# heap.push(5)
# heap.display_Heap()
# heap.delete_min()
# heap.display_Heap()
# heap.decrease_key(1, 1)
# heap.display_Heap()
# heap.delete_key(0)
# heap.display_Heap()
# print(heap.size())
for i in range(0, 20):
    heap.push(i)

heap.display_Heap()

print(heap.delete_min())

heap.change_key(3, 10000)

heap.display_Heap()
