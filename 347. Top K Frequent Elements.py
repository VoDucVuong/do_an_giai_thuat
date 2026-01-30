from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        result = sorted(count, key=count.get, reverse=True)
        return result[:k]