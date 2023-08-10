# Link For Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = nums1, nums2

        total: int = len(nums1)+len(nums2)
        half: int = total//2

        if len(b) < len(a):
            a, b = b, a

        left, right = 0, len(a)-1

        while True:
            i: int = (left+right)//2  # a
            j: int = half-i-2  # b

            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i+1] if (i+1) < len(a) else float("infinity")

            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j+1] if (j+1) < len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright))//2

            elif Aleft > Bright:
                right = i-1

            else:
                left = i+1
