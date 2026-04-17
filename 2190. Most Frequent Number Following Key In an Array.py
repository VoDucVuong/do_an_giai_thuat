class Solution(object):
    def mostFrequent(self, nums, key):
        count = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] in count:
                    count[nums[i+1]] +=1
                else:
                    count[nums[i+1]] = 1
        result = max(count, key = count.get)
        return result