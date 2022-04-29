# Link For Problem : https://leetcode.com/problems/isomorphic-strings/


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}

        for c1, c2 in zip(s, t):

            if (c1 not in st) and (c2 not in ts):
                st[c1] = c2
                ts[c2] = c1

            elif st.get(c1) != c2 or ts.get(c2) != c1:
                return False

        return True

    def another_solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp = {}

        for c1, c2 in zip(s, t):

            if c1 not in tmp:
                tmp[c1] = c2

            else:
                if tmp[c1] != c2:
                    return False
                else:
                    continue

        if len(list(set(tmp.values()))) != len(tmp.values()):
            return False

        return True
