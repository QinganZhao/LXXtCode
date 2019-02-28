class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        for i in range(len(s)):
            if dic1[s[i]] != t[i] or dic2[t[i]] != s[i]:
                return False
        return True
