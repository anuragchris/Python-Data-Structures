# Link For Problem : https://leetcode.com/problems/min-stack/

class MinStack:
    st = []
    min = []

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if(len(self.min) == 0 or self.min[-1] >= val):
            self.min.append(val)

    def pop(self) -> None:
        temp = self.st.pop()

        if(self.min[-1] == temp):
            self.min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if len(self.min) == 0:
            return -1
        return self.min[-1]
