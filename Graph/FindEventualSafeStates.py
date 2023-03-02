# Link For Problem: https://leetcode.com/problems/find-eventual-safe-states/

class Solution:

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe = {}

        def dfs(i: int) -> bool:
            if i in safe:
                return safe[i]

            safe[i] = False

            for neighour in graph[i]:
                if not dfs(neighour):
                    return False

            safe[i] = True

            return True

        res = []

        for i in range(n):
            if dfs(i):
                res.append(i)

        return res
