# Link For Problem: https://leetcode.com/problems/redundant-connection/

class Solution:

    def find(self, x: int, parent: list[int]) -> int:
        if parent[x] == -1:
            return x

        parent[x] = self.find(parent[x], parent)

        return parent[x]

    def union(self, x: int, y: int, parent: list[int], rank: list[int]) -> bool:
        root_x, root_y = self.find(x, parent), self.find(y, parent)

        if root_x == root_y:
            return False

        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
            rank[root_y] += 1
            return True

        else:
            parent[root_y] = root_x
            rank[root_x] += 1
            return True

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent: list[int] = [-1] * (len(edges)+1)
        rank: list[int] = [0] * (len(edges)+1)

        for x, y in edges:
            if not self.union(x, y, parent, rank):
                return [x, y]
