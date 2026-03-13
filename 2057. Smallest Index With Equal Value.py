class Solution(object):
    def smallestEqual(self, nums):
        for idx, n in enumerate(nums):
            if idx % 10 == n:
                return idx
        return -1