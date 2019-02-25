class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if int(n) != n:
            return False
        return self.isPowerOfTwo(n/2)
