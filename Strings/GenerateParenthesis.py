# Link For Problem: https://leetcode.com/problems/generate-parentheses/


class Solution:

    def solve(self, ans: list, s: list, open: int, close: int, n: int) -> None:
        if len(s) == 2*n:
            ans.append("".join(s))
            return

        if open < n:
            s.append("(")
            self.solve(ans, s, open+1, close, n)
            s.pop()

        if close < open:
            s.append(")")
            self.solve(ans, s, open, close+1, n)
            s.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        ans, s = [], []
        self.solve(ans, s, 0, 0, n)

        return ans

    def another_solution(self, n: int) -> list[str]:
        ans = []

        def backtrack(S: list = [], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return

            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()

            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()

        backtrack()

        return ans
