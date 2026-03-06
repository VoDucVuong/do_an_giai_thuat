class Solution(object):
    def sortPeople(self, names, heights):
        length = len(heights)
        map = {}
        for i in range(length):
            map[heights[i]]= names[i]
        heights.sort(reverse = True)
        res = []
        for height in heights:
            res.append(map[height])
        return res