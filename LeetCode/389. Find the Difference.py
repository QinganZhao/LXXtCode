class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            if char not in dic or not dic[char]:
                return char
            dic[char] -= 1
