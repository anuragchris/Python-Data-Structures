class BubbleSort:

    def bubbleSort(self, arr: list[int]) -> None:

        for i in range(len(arr)-1, -1, -1):

            for j in range(i):

                if arr[j] > arr[j+1]:
                    temp: int = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

    def checkAlreadySorted(self, arr: list[int]) -> bool:
        swap: bool = False

        for i in range(len(arr)-1, -1, -1):

            for j in range(i):

                if arr[j] > arr[j+1]:
                    temp: int = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    swap = True

            if not swap:
                break

        return not swap


check = BubbleSort()
arr = [2, 1, 5, 8, 7, 9, 0]

check.bubbleSort(arr)
print(arr)
print(check.checkAlreadySorted(arr))
