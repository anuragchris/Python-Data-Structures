# Link For Problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        elif root.val > val:

            if root.left:
                root.left = self.insertIntoBST(root.left, val)

            else:
                root.left = TreeNode(val)

        else:

            if root.right:
                root.right = self.insertIntoBST(root.right, val)

            else:
                root.right = TreeNode(val)

        return root
