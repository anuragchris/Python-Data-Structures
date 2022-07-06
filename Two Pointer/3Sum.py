# Link For Problem: https://leetcode.com/problems/3sum/

class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        if nums[0] > 0:
            return []

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            low, high = i+1, len(nums)-1
            temp = 0

            while(low < high):
                temp = nums[i]+nums[low]+nums[high]

                if temp > 0:
                    high -= 1

                elif temp < 0:
                    low += 1

                else:
                    ans.append([nums[i], nums[low], nums[high]])

                    lastLow, lastHigh = nums[low], nums[high]

                    while low < high and lastLow == nums[low]:
                        low += 1

                    while low < high and lastHigh == nums[high]:
                        high -= 1

        return ans

    def another_solution(self, nums: list[int]) -> list[list[int]]:
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:

            if num > 0:
                p.append(num)

            elif num < 0:
                n.append(num)

            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
