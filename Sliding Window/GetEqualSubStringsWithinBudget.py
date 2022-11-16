# Link For Problem: https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i: int = 0
        j: int = 0

        for a, b in zip(s, t):
            maxCost -= abs(ord(a)-ord(b))

            if maxCost < 0:
                maxCost += abs(ord(s[i])-ord(t[i]))
                i += 1

            j += 1

        return j-i
