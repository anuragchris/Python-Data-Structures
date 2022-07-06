# Link For Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead: ListNode = head

        while newHead.next:

            if newHead.val == newHead.next.val:
                newHead.next = newHead.next.next

            else:
                newHead = newHead.next

        return head
