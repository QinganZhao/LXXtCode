class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        Dict = {}
        i = 0
        result = 0
        for j in range(n):
            if s[j] in Dict:
                i = max(Dict[s[j]], i)
            result = max(result, j - i + 1)
            Dict[s[j]] = j + 1
        return result
            
                
                
        
