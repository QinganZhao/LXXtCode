class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        String = str(x)
        mark = len(String) - 1
        newString = ''
        for i in range(len(String)):
            newString += String[mark]
            mark -= 1
        
        if newString[-1] == '-':
            return False
        else:
            xrev = int(newString)
            if xrev == x:
                return True
            else:
                return False
            
        