class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1
