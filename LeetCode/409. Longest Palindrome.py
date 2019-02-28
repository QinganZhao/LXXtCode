class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        res = 0
        numList = sorted(list(map(lambda x: x[1], dic.items())),
                         reverse = True)
        mark = 0
        for num in numList:
            if not num % 2:
                res += num
            elif num % 2 and not mark:
                res += num
                mark += 1
            else:
                res += (num - 1)
        return res
