class Solution:
    def getSum(self, a: int, b: int) -> int:
        maxBin = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a <= maxBin:
            return a
        else:
            # In Python, negative binary numbers are represented
            # by 32-bit positive's complement
            return ~(a ^ mask)
