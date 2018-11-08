class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ''
        for i in range(numRows):
            for j in range(i, len(s), 2*(numRows-1)):
                res += s[j]
                if i != 0 and i != numRows-1 and j+2*(numRows-i-1)<len(s):
                    res += s[j+2*(numRows-i-1)]
                    
        return res
                    
                
        
