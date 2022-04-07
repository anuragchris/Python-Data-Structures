# Link For Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def search(self, current: TreeNode, max: int) -> int:
        if not current:
            return 0

        count: int = 0
        if current.val >= max:
            count += 1
            max = current.val

        if current.left:
            count += self.search(current.left, max)

        if current.right:
            count += self.search(current.right, max)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        goodNodes: int = 1  # Include Root

        goodNodes += self.search(root.left, root.val)
        goodNodes += self.search(root.right, root.val)

        return goodNodes
