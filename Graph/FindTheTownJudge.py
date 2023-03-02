# Link For Problem: https://leetcode.com/problems/find-the-town-judge/

class Solution:

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1

        if len(trust) == 0:
            return -1

        people: list[int] = [0]*(n + 1)

        for t in trust:
            people[t[0]] -= 1

            people[t[1]] += 1

        for p in range(len(people)):
            if people[p] == n-1:
                return p

        return -1


s = Solution()

trust = [[1, 2]]
n = 2

print(s.findJudge(n, trust))
