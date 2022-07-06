# Link For Problem: https://leetcode.com/problems/circular-array-loop/

class Solution:

    def getNextPosition(self, arr: list[int], index: int, iforward: bool) -> int:
        direction: bool = arr[index] >= 0

        if direction != iforward:
            return -1

        nextIndex: int = (index+arr[index]) % len(arr)

        if nextIndex < 0:
            nextIndex += len(arr)

        if nextIndex == index:
            return -1

        return nextIndex

    def circularArrayLoop(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            slow, fast = i, i
            iforward: bool = nums[i] > 0

            while True:
                slow = self.getNextPosition(nums, slow, iforward)

                if slow == -1:
                    break

                fast = self.getNextPosition(nums, fast, iforward)

                if fast == -1:
                    break

                fast = self.getNextPosition(nums, fast, iforward)

                if fast == -1:
                    break

                if slow == fast:
                    return True

        return False
