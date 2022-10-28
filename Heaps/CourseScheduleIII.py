# Link For Problem: https://leetcode.com/problems/course-schedule-iii/

import heapq


class Solution:

    def scheduleCourse(self, courses: list[list[int]]) -> int:
        heap = []
        time = 0

        for dur, end in sorted(courses, key=lambda x: x[1]):
            time += dur

            heapq.heappush(heap, -dur)

            if time > end:
                time += heapq.heappop(heap)

        return len(heap)
