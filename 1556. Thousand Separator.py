class Solution(object):
    def thousandSeparator(self, n):
        n = str(n)
        for i in range(len(n)-3, 0, -3):
            n = str(n)[:i] + "."+str(n)[i:]
        return n
        