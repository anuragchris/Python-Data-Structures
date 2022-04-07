# Link For Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: TreeNode, val: int) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return (val*10) + root.val

        return self.dfs(root.left, (val*10)+root.val) + self.dfs(root.right, (val*10)+root.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.dfs(root, 0)
