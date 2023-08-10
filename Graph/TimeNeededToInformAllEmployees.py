# Link For Problem: https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        children = [[] for i in range(n)]

        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        return dfs(headID)

    def anotherSolution(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])

                manager[i] = -1

            return informTime[i]

        return max(map(dfs, range(n)))
