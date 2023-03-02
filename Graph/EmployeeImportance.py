# Link For Problem: https://leetcode.com/problems/employee-importance/

from collections import deque


class Employee:

    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:

    def getImportance(self, employees: list['Employee'], id: int) -> int:
        map = {emp.id: emp for emp in employees}

        def dfs(eid: int) -> int:
            emp: Employee = map[eid]
            ans: int = emp.importance

            for sumId in emp.subordinates:
                ans += dfs(sumId)

            return ans

        return dfs(id)

    def bfs(self, employees: list['Employee'], id: int) -> int:
        map = {emp.id: emp for emp in employees}

        q = deque()
        q.appendleft(map[id])

        res: int = 0

        while q:
            emp: Employee = q.popleft()
            res += emp.importance

            for subId in emp.subordinates:
                q.append(map[subId])

        return res
