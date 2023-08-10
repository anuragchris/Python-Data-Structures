class SelectionSort:

    def selectionSort(self, arr: list[int]) -> None:

        for i in range(len(arr)):
            minimum: int = i

            for j in range(i+1, (len(arr))):
                if arr[j] < arr[minimum]:
                    minimum = j

            if minimum != i:
                temp: int = arr[i]
                arr[i] = arr[minimum]
                arr[minimum] = temp


check = SelectionSort()
arr = [2, 6, 4, 9, 1, 0]
check.selectionSort(arr)
print(arr)
