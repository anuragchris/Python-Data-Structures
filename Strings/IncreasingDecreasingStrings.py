# Link For Problem: https://leetcode.com/problems/increasing-decreasing-string/

import collections
import string


class Solution:

    def sortString(self, s: str) -> str:
        result = []
        counter = collections.Counter(s)

        while len(result) < len(s):

            for sequence in [string.ascii_lowercase, string.ascii_lowercase[::-1]]:

                for ch in sequence:

                    if counter[ch] > 0:
                        result.append(ch)
                        counter[ch] -= 1

        return "".join(result)

    def another_solution(self, s: str) -> str:
        dict1 = {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        ans = ""
        flag = 0

        asc = sorted(dict1.keys())
        dsc = asc[::-1]

        while(True):
            temp = ans

            if flag == 0:
                for i in asc:

                    if dict1[i] >= 1:
                        ans += i
                        dict1[i] -= 1

                flag = 1

            else:
                for i in dsc:

                    if dict1[i] >= 1:
                        ans += i
                        dict1[i] -= 1

                flag = 0

            if temp == ans:
                break

        return ans
