# Link For Problem: https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
