class Solution(object):
    def pivotInteger(self, n):
        ans = -1
        for num in range(n+1):
            left = sum(range(1,num+1))
            right = sum(range(num,n+1))
            if left == right:
                return num
        return -1
        