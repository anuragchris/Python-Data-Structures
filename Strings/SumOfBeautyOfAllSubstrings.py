# Link For Problem: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

from collections import defaultdict


class Solution:

    def beautySum(self, s: str) -> int:
        ans: int = 0

        for i in range(len(s)):
            arr = defaultdict(int)

            for j in range(i, len(s)):
                arr[ord(s[j])-ord('a')] += 1

                if(len(list(arr.values())) == 0):
                    continue

                mx, mn = max(arr.values()), min(arr.values())
                ans += mx-mn

        return ans

    def another_solution(self, s: str) -> int:
        res = 0

        for i, x in enumerate(s):
            cntr = defaultdict(lambda: 0)
            cntr[x] = 1

            for j in range(i+1, len(s)):
                curr = s[j]
                cntr[curr] += 1

                val = list(cntr.values())

                if(len(val) == 0):
                    continue

                val.sort()
                res += val[-1] - val[0]

        return res
