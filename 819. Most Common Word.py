class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        dict = {}
        banned = set(banned)
        for c in "!?',.;":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                if word in dict:
                    dict[word]+=1
                else:
                    dict[word]=1
        return max(dict, key= dict.get)