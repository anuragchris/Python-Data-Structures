# Link For Problem : https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict, deque


class Graph:
    vertexCount: int
    adjList: defaultdict(list)

    def __init__(self, v: int) -> None:
        self.vertexCount = v
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjList[u].append(v)


class Solution:

    def isCyclicUtil(self, current: int, visited: list[bool], recStack: list[bool], adjList: defaultdict(list)) -> bool:
        if recStack[current]:
            return True

        if visited[current]:
            return False

        visited[current], recStack[current] = True, True

        for i in adjList[current]:
            if self.isCyclicUtil(i, visited, recStack, adjList):
                return True

        recStack[current] = False

        return False

    def isCyclic(self, graph: Graph) -> bool:
        visited: list[bool] = [False]*graph.vertexCount
        recStack: list[bool] = [False]*graph.vertexCount

        for i in range(graph.vertexCount):
            if self.isCyclicUtil(i, visited, recStack, graph.adjList):
                return True

        return False

    def topologicalSortUtil(self, current: int, visited: list[bool], stack: list[int], adjList: defaultdict(list)) -> None:
        visited[current] = True

        for i in adjList[current]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack, adjList)

        stack.append(current)

    def topologicalSort(self, graph: Graph) -> list[int]:
        visited: list[bool] = [False]*graph.vertexCount
        stack: list[int] = []

        for i in range(graph.vertexCount):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack, graph.adjList)

        return stack[::-1]

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = Graph(numCourses)

        for pre in prerequisites:
            graph.addEdge(pre[1], pre[0])

        ans: list[int] = []

        if self.isCyclic(graph):
            return ans
        else:
            return self.topologicalSort(graph)

    def anotherSolution(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        in_degree = [0] * numCourses
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        schedule = []
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            course = queue.popleft()
            schedule.append(course)

            for next_course in adj_list[course]:
                in_degree[next_course] -= 1

                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return schedule if len(schedule) == numCourses else []
