class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        sList = str.split()
        if len(pattern) != len(sList):
            return False
        dicP = {}
        dicS = {}
        for i in range(len(pattern)):
            dicS[pattern[i]] = sList[i]
            dicP[sList[i]] = pattern[i]
        for i in range(len(pattern)):
            if dicS[pattern[i]] != sList[i] or dicP[sList[i]] != pattern[i]:
                return False
        return True
        
        return p1 == p2
