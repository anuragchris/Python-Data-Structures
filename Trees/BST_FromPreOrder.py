# Link For Problem: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    i: int = 0

    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:

        def buildBST(preOrder: list[int], bound: int) -> TreeNode:

            if self.i == len(preOrder) or preOrder[self.i] > bound:
                return None

            root: TreeNode = TreeNode(val=preOrder[self.i])
            self.i += 1

            root.left = buildBST(preOrder, root.val)
            root.right = buildBST(preOrder, bound)

            return root

        return buildBST(preorder, sys.maxsize-1)

    # def buildBST(self, preOrder: list[int], bound: int) -> TreeNode:

    #     if self.i == len(preOrder) or preOrder[self.i] > bound:
    #         return None

    #     root: TreeNode = preOrder[self.i]
    #     self.i += 1

    #     root.left = self.buildBST(preOrder, root.val)
    #     root.right = self.buildBST(preOrder, bound)

    #     return root
