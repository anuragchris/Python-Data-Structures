# Link For Problem: https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def countNodesOptimized(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_level: int = 1
        left_node: TreeNode = root.left

        while(left_node):
            left_node = left_node.left
            left_level += 1

        right_level = 1
        right_node: TreeNode = root.right

        while(right_node):
            right_node = right_node.right
            right_level += 1

        if left_level == right_level:
            return (2**left_level)-1

        return 1+self.countNodesOptimized(root.left)+self.countNodesOptimized(root.right)
