class Solution(object):
    def sortEvenOdd(self, nums):
        if len(nums) == 2:
            return nums
        else:
            evensorted = []
            oddsorted = []
            for i in range(len(nums)):
                if i%2 == 0:
                    evensorted.append(nums[i])
                else:
                    oddsorted.append(nums[i])
            evensorted.sort()
            oddsorted.sort(reverse=True)
            
            evenindex = 0
            oddindex = 0
            for i in range(len(nums)):
                if i%2==0:
                    nums[i] = evensorted[evenindex]
                    evenindex += 1
                else:
                    nums[i] = oddsorted[oddindex]
                    oddindex += 1
        return nums
        