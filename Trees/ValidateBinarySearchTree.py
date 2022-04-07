# Link For Problem: https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.checkBST(root, None, None)

    def checkBST(self, root: TreeNode, min: TreeNode, max: TreeNode) -> bool:
        if not root:
            return True

        if min and root.val <= min.val:
            return False

        if max and root.val >= max.val:
            return False

        return self.checkBST(root.left, min, root) and self.checkBST(root.right, root, max)
