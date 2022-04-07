# Link For Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left: TreeNode = self.lowestCommonAncestor(root.left, p, q)
        right: TreeNode = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right

        elif not right:
            return left

        return root
