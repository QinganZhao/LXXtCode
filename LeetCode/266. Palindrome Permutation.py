class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        numList = list(map(lambda x: x[1], dic.items()))
        mark = 0
        for i in numList:
            if not mark and i % 2:
                mark = 1
            elif i % 2:
                return False
        return True
