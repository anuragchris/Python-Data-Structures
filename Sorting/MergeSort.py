class MergeSort:

    def merge(self, arr: list[int], l: list[int], r: list[int], left: int, right: int) -> None:
        i, j, k = 0, 0, 0

        while i < left and j < right:

            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1

            k += 1

        while i < left:
            arr[k] = l[i]
            k += 1
            i += 1

        while j < right:
            arr[k] = r[j]
            k += 1
            j += 1

    def mergeSort(self, arr: list[int], n: int) -> None:
        if n < 2:
            return

        mid: int = n//2

        l, r = [0 for i in range(mid)], [0 for i in range(n-mid)]

        for i in range(mid):
            l[i] = arr[i]

        for i in range(mid, n):
            r[i-mid] = arr[i]

        self.mergeSort(l, mid)
        self.mergeSort(r, n-mid)

        self.merge(arr, l, r, mid, n-mid)


check = MergeSort()
arr = [1, 5, 2, 7, 4, 9, 8, 8, 0, 6, 3]
check.mergeSort(arr, len(arr))
print(arr)
