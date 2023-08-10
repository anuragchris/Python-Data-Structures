class QuickSort:

    def partition(self, arr: list[int], left: int, right: int) -> int:
        pivot: int = arr[left]
        start, end = left, right

        while start < end:

            while arr[start] <= pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start < end:
                temp: int = arr[start]
                arr[start] = arr[end]
                arr[end] = temp

        temp: int = arr[left]
        arr[left] = arr[end]
        arr[end] = temp

        return end

    def quickSort(self, arr: list[int], low: int, high: int) -> None:
        if low < high:
            pi: int = self.partition(arr, low, high)

            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)


check = QuickSort()
arr = [1, 9, 8, 0, 4, 7, 2, 0]
check.quickSort(arr, 0, len(arr)-1)
print(arr)
