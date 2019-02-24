class Solution:
    def titleToNumber(self, s: str) -> int:
        Alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        num = [i for i in range(1, 27)]
        Dict = dict(zip(Alpha, num))
        res = 0
        for i, char in enumerate(reversed(s)):
            res += 26 ** i * Dict[char]
        return res
