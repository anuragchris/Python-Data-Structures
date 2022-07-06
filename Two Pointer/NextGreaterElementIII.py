# Link For Problem: https://leetcode.com/problems/next-greater-element-iii/

class Solution:

    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))

        i: int = len(arr)-2

        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1

        if i == -1:
            return -1

        k: int = len(arr)-1

        while arr[k] <= arr[i]:
            k -= 1

        arr[i], arr[k] = arr[k], arr[i]

        ans = []

        for j in range(i+1):
            ans.append(arr[j])

        for j in range(len(arr)-1, i, -1):
            ans.append(arr[j])

        ans_ = int(''.join(ans))

        return ans_ if ans_ < 2**31 else -1
