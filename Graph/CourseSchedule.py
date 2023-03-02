# Link For Problem : https://leetcode.com/problems/course-schedule/

from collections import defaultdict


class Solution:

    def isCyclic(self, adj_List: defaultdict(list), visited: list[bool], helper: list[bool], i: int) -> bool:
        if helper[i]:
            return True

        if visited[i]:
            return False

        visited[i], helper[i] = True, True

        for next_course in adj_List[i]:
            if self.isCyclic(adj_List, visited, helper, next_course):
                return True

        helper[i] = False

        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_List = defaultdict(list)

        for course, pre in prerequisites:
            adj_List[pre].append(course)

        visited: list[bool] = [False]*numCourses
        helper: list[bool] = [False]*numCourses

        for i in range(numCourses):

            if not visited[i]:
                if self.isCyclic(adj_List, visited, helper, i):
                    return False

        return True
