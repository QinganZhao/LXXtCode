class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        new = [0] * 2 * len(s)
        Max = 0
        Dict = {}
        for i in range(len(new)):
            if not i % 2:
                new[i] = '#'
            else:
                new[i] = s[int((i-1)/2)]
        for i in range(len(new)):
            count = 0
            for j in range(1, len(new)):
                if i-j < 0 or i+j >= len(new):
                    break
                if new[i-j] != new[i+j]:
                    break
                count += 1
            Dict[count] = i
            Max = max(Max, count)
        for i in Dict.keys():
            if i == Max:
                medium = Dict[i]
                break
        res = [new[i] for i in range(medium-Max, medium+Max+1)]
        res = ''.join([res[i] for i in range(2*Max+1) if res[i] != '#'])
        return res
            
            
                
                
                
            
                
            
            
        
