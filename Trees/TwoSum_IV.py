# Link For Problem: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def helper(self, root: TreeNode, k: int, my_set: set, ans: bool) -> bool:
        if not root:
            return False

        diff: int = k-root.val
        if diff in my_set:
            return True

        my_set.add(root.val)

        if not ans and root.left:
            ans = self.helper(root.left, k, my_set, ans)

        if not ans and root.right:
            ans = self.helper(root.right, k, my_set, ans)

        return ans

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        my_set: set = set()

        return self.helper(root, k, my_set, False)

    # BFS Solution

    def bfs(self, root: Optional[TreeNode], k: int) -> bool:
        q = []
        my_set: set = set()
        q.append(root)

        while q:
            current: TreeNode = q.pop(0)

            if (k-current.val) in my_set:
                return True

            my_set.add(current.val)

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)

        return False
