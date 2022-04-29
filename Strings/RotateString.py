# Link For Problem : https://leetcode.com/problems/rotate-string/

from collections import deque


class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and (s+s).find(goal) != -1

    def another_solution(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s

    def using_queue(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        q1 = deque()
        for i in s:
            q1.append(i)

        q2 = deque()
        for i in goal:
            q2.append(i)

        k: int = len(goal)

        while(k > 0):
            k -= 1

            ch = q2.popleft()
            q2.append(ch)

            if(q2 == q1):
                return True

        return False

    def using_kmp(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return self.kmp(s+s, goal)

    def build_lps(self, s: str) -> list[int]:
        lps = [0]*len(s)
        idx: int = 0

        for i in range(1, len(s)):

            if(s[i] == s[idx]):
                lps[i] = idx+1
                i += 1
                idx += 1

            else:

                if(idx != 0):
                    idx = lps[idx-1]

                else:
                    lps[i] = 0
                    i += 1

        return lps

    def kmp(self, s: str, goal: str) -> bool:
        lps = self.build_lps(s)
        i, j = 0, 0

        while i < len(s) and j < len(goal):

            if s[i] == goal[j]:
                i += 1
                j += 1

            else:

                if j != 0:
                    j = lps[j-1]

                else:
                    i += 1

        return j == len(goal)
