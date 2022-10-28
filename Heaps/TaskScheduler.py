# Link For Problem: https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:

    def leastInterval(self, tasks: list[str], n: int) -> int:
        count: dict = Counter(tasks)

        maxHeap: list = [-cnt for cnt in count.values()]
        heapify(maxHeap)

        time: int = 0
        q: deque = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt: int = 1+heappop(maxHeap)

                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])

        return time
