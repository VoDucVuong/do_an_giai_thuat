class Solution(object):
    def distributeCandies(self, candyType):
        s = set(candyType)
        if len(s) <= len(candyType)/2:
            return len(s)
        return len(candyType)/2