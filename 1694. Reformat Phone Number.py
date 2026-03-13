class Solution(object):
    def reformatNumber(self, number):
        res, count = [], 0
        for x in number:
            if x.isdigit():
                if count == 3:
                    res.append("-")
                    count = 0
                res.append(x)
                count +=1
        if count == 1: res[-2], res[-3] = res[-3], res[-2]
        return "".join(res)