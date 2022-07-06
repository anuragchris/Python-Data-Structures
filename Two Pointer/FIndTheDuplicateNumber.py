# Link For Problem: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:

    def findDuplicate(self, nums: list[int]) -> int:
        duplicate: int = -1

        for i in range(len(nums)):
            current: int = abs(nums[i])

            if(nums[current] < 0):
                duplicate = current
                break

            nums[current] *= -1

        for i in range(len(nums)):
            nums[i] *= -1

        return duplicate

    def floydCycleDetection(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

    def another_solution(self, nums: list[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
