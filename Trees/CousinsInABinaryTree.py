# Link For Problem: https://leetcode.com/problems/cousins-in-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if not root:
            return False

        q = deque([root])

        while q:
            size: int = len(q)
            map = {}

            for i in range(size):
                current: TreeNode = q.popleft()

                if current.left:
                    q.append(current.left)
                    map[current.left.val] = current.val

                if current.right:
                    q.append(current.right)
                    map[current.right.val] = current.val

                if x in map and y in map and map[x] != map[y]:
                    return True

        return False

    def anotherSolution(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if not root:
            return False

        q = deque()
        q.append(root)

        x = y = False

        while q:

            for _ in range(len(q)):
                current: TreeNode = q.popleft()

                if current.left:
                    if current.left.val == x:
                        x = True

                    if current.left.val == y:
                        y = True

                    q.append(current.left)

                if current.right:
                    if current.right.val == x:
                        x = True

                    if current.right.val == y:
                        y = True

                    q.append(current.right)

                if x and y:
                    return not((current.left and current.left.val == x and current.right and current.right.val == y) or (current.left and current.left.val == y and current.right and current.right.val == x))

            if x or y:
                return False
