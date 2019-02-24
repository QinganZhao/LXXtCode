class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        Alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        while n:
            res = Alpha[(n-1) % 26] + res
            n = (n-1) // 26
        return res
