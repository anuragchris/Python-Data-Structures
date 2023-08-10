class InsertionSort:

    def InsertionSort(self, arr: list[int]) -> None:

        for i in range(1, len(arr)):
            key: int = arr[i]

            while(arr[i-1] > key and i >= 1):
                arr[i] = arr[i-1]
                i -= 1

            arr[i] = key


check = InsertionSort()
arr = [2, 6, 4, 9, 1, 0]
check.InsertionSort(arr)
print(arr)
