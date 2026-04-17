class Solution(object):
    def findClosestNumber(self, nums):
        best = nums[0]
        for n in nums:
            if abs(n-0.1) < abs(best-0.1):
                best =n
        return best
        