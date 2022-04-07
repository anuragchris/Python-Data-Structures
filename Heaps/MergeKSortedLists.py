# Link For Problem: https://leetcode.com/problems/merge-k-sorted-lists/

from queue import PriorityQueue
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        result: list[ListNode] = []

        for segment in lists:
            node = segment

            while(node):
                result.append(node)
                node = node.next

        if result == []:
            return None

        result.sort(key=lambda x: x.val)

        for idx in range(0, len(result)-1):
            result[idx].next = result[idx+1]

        result[-1].next = None

        return result[0]

    def usingPriorityQueue(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        node_queue = PriorityQueue(len(list))

        counter: int = 1

        for node in lists:
            if node:
                node_queue.put((node.val, counter, node))
                counter += 1

        dummy: ListNode = ListNode(0, None)
        current: ListNode = dummy

        while not node_queue.empty():
            _, _, temp = node_queue.get()
            current.next = temp
            current = current.next

            if temp.next:
                node_queue.put((temp.next.val, counter, temp.next))
                counter += 1

        return dummy.next
