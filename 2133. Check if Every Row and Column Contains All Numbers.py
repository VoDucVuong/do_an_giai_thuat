class Solution(object):
    def checkValid(self, matrix):
        return all(len(matrix) == len(set(x)) for x in matrix + list(zip(*matrix)))