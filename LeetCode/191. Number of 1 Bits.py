### string approach
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binStr = '{0:{fill}32b}'.format(n, fill='0')
        res = 0
        for i in binStr:
            if i == '1':
                res += 1
        return res
    
### bit manipulation
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res
