class Solution(object):
    def pickGifts(self, gifts, k):
        for _ in range(k):
            largest = max(gifts)                 
            index = gifts.index(largest)         
            gifts[index] = int(math.sqrt(largest))   

        return sum(gifts)