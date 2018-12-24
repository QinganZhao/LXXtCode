class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
        Integer = 0
        for i in xrange(len(s)):
            if i > 0 and romanMap[s[i]] > romanMap[s[i-1]]:
                Integer += romanMap[s[i]] - 2 * romanMap[s[i-1]]
            else:
                Integer += romanMap[s[i]]
                
        return Integer
        
