# Link For Problem: https://leetcode.com/problems/evaluate-division/

from collections import defaultdict


class Solution:

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)

        for i, (var1, var2) in enumerate(equations):
            graph[var1].append((var2, values[i]))
            graph[var2].append((var1, 1.0/values[i]))

        def dfs(node, target, product, visited):
            if n not in graph or d not in graph:
                return -1

            if node == target:
                return product

            visited.add(node)

            for neighour, quotient in graph[node]:

                if neighour not in visited:
                    soln = dfs(neighour, target, product*quotient, visited)

                    if soln != -1:
                        return soln

            return -1

        res = []

        for n, d in queries:
            res.append(dfs(n, d, 1, set()))

        return res
