# Link For Problem: https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:

    def count(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0

        n, total, diff, j = len(nums), 0, 0, 0

        count: list[int] = [0]*20002

        for i in range(n):
            if count[nums[i]] == 0:
                diff += 1

            count[nums[i]] += 1

            if diff <= k:
                total += i-j+1

            else:
                while j < n and j < i and diff > k:
                    count[nums[j]] -= 1

                    if count[nums[j]] == 0:
                        diff -= 1

                    j += 1

                total += i-j+1

        return total

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.count(nums, k)-self.count(nums, k-1)
