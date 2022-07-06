# Link For Problem: https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        prev, temp = ListNode(), ListNode()

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        fast = head
        slow = prev

        while slow:

            if slow.val != fast.val:
                return False

            fast = fast.next
            slow = slow.next

        return True
