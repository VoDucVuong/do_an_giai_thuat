class Solution(object):
    def minimumMoves(self, s):
        s = list(s)
        n = len(s)
        c= 0
        i = 0
        j = 2
        while i < n:
            if s[i] == 'O':
                i+=1
                j+=1
            elif s[i] == 'X':
                c+=1
                i+=3
                j+=3
        return c
        