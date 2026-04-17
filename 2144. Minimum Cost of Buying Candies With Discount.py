class Solution(object):
    def minimumCost(self, cost):
        return sum(cost) - sum(sorted(cost) [-3::-3])