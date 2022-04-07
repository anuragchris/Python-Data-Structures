# Link For Problem: https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(root: TreeNode) -> int:
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            res[0] = max(res[0], left+right)

            return 1+max(left, right)

        res = [0]
        depth(root)

        return res[0]
