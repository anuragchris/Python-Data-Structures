# Link For Problem : https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from typing import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0

        a, b = {}, {}

        for i in s:

            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        for i in t:

            if i not in b:
                b[i] = 1
            else:
                b[i] += 1

        for ch in a:

            if ch in b:

                if b[ch] > a[ch]:
                    b[ch] = b[ch]-a[ch]
                else:
                    b.pop(ch)

        count: int = 0
        for i in b.values():
            count += i

        return count

    def another_solution(self, s: str, t: str) -> int:
        if s == t:
            return 0

        a: dict = Counter(s)

        result = 0

        for c in t:
            if c not in a or a[c] == 0:
                result += 1
            else:
                a[c] -= 1

        return result

    def optimized(self, s: str, t: str) -> int:
        return sum(max(s.count(c) - t.count(c), 0) for c in set(s))
