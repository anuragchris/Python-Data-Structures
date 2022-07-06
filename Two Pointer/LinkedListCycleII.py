# Link For Problem: https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return head
