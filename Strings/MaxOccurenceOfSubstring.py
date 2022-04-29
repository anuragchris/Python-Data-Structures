# Link For Problem: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

from collections import defaultdict


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        final = {}
        q, n = [], len(s)

        for i in range(0, n):
            q.append(s[i])

            if len(q) <= maxSize and len(q) >= minSize:

                if len(set(q)) <= maxLetters:
                    a = "".join(q)

                    if a not in final:
                        final[a] = 1
                    else:
                        final[a] += 1

                q.pop(0)

        maxoccurence = 0

        for i, v in enumerate(final):
            maxoccurence = max(final[v], maxoccurence)

        return maxoccurence

    def another_solution(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        C = defaultdict(int)

        for i in range(len(s)-minSize+1):

            if len(set(s[i:i+minSize])) <= maxLetters:
                C[s[i:i+minSize]] += 1

        return max(C.values()) if C else 0
