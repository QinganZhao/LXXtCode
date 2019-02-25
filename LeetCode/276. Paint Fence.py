class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n:
            return 0
        if n == 1:
            return k
        same, diff = k, k * (k - 1)
        for i in range(2, n):
            same, diff = diff, (same + diff) * (k - 1)  
        return same + diff
