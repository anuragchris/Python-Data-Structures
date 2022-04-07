# Link For Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None

        st = []

        while True:

            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            k -= 1

            if not k:
                return root.val

            root = root.right
