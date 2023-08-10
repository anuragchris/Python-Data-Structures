class CountingSort:

    def countElements(self, arr: list[int], k: int) -> list[int]:
        res: list[int] = [0 for i in range(k+1)]

        for i in arr:
            res[i] += 1

        for i in range(1, len(res)):
            res[i] += res[i-1]

        return res

    def sort(self, arr: list[int]) -> None:
        k: int = max(arr)

        c: list[int] = self.countElements(arr, k)

        ans: list[int] = [0 for i in range(len(arr))]

        for i in range(len(arr)-1, -1, -1):
            j: int = arr[i]
            ans[c[j]-1] = j
            c[j] -= 1

        return ans


check = CountingSort()
arr = [2, 6, 4, 9, 1, 0]
print(check.sort(arr))
