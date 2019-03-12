class Solution:
    def validPalindrome(self, s: str) -> bool:
        mark, i, j = 0, 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                if mark == 2:
                    return False
                if mark == 1:
                    i, j = cache
                    j -= 1
                else:
                    cache = (i, j)
                    i += 1
                mark += 1
            else:
                i += 1
                j -= 1
        return True
