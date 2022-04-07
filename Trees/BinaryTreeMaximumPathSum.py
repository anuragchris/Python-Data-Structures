# Link For Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/

import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    result: int = (-sys.maxsize)+1

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxPathSumutil(root: TreeNode) -> int:
            if not root:
                return 0

            left: int = maxPathSumutil(root.left)
            right: int = maxPathSumutil(root.right)

            straight: int = max(max(left, right)+root.val, root.val)
            case2: int = max(straight, left+right+root.val)

            self.result = max(case2, self.result)

            return straight

        maxPathSumutil(root)

        return self.result
