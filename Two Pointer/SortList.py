# Link For Problem: https://leetcode.com/problems/sort-list/

from typing import List, Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getMid(self, head: ListNode) -> ListNode:
        prev: ListNode = None

        while head and head.next:

            if not prev:
                prev = head
            else:
                prev = prev.next

            head = head.next.next

        mid: ListNode = prev.next
        prev.next = None

        return mid

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy: ListNode = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next

        if not l1:
            tail.next = l2
        else:
            tail.next = l1

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid: ListNode = self.getMid(head)
        left: ListNode = self.sortList(head)
        right: ListNode = self.sortList(mid)

        return self.merge(left, right)
