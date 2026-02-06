class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        return [pattern.index(c) for c in pattern] == [words.index(w) for w in words]