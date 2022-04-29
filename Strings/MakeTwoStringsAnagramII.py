# Link For Problem: https: // leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        a = [0]*26

        for i in s:
            a[ord(i)-ord('a')] += 1

        for i in t:
            a[ord(i)-ord('a')] -= 1

        count: int = 0
        for i in a:
            count += abs(i)

        return count

    def another_solution(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        res = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            res += abs(s_counter[ch] - t_counter[ch])

        return res
