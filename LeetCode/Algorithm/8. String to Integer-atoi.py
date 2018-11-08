class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digit = {'0','1','2','3','4','5','6','7','8','9'}
        mark = {'+', '-'}
        res = ''
        isNum = False
        for ind, char in enumerate(str):
            if char == ' ':
                continue
            if char in digit:
                isNum = True
                break
            elif char in mark and ind < len(str)-1 and str[ind+1] in digit:
                isNum = True
                break
            else:
                break
        if not isNum:
            return 0
        res += char
        for i in range(ind+1, len(str)):
            if str[i] not in digit:
                break
            res += str[i]
        Num = int(res)
        if Num < -2**31:
            return -2**31
        if Num > 2**31-1:
            return 2**31-1
        return Num
            
                
                
            
        
        
