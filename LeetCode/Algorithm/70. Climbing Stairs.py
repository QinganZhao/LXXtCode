class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            OPT = [0] * n
            OPT[0] = 1
            OPT[1] = 2
            for i in range(2, n):
                OPT[i] = OPT[i-1] + OPT[i-2]
            return OPT[n-1]
