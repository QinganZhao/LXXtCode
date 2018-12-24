class Solution:
    
    if False:
    # iteration
        def letterCombinations(self, digits):
            if not digits:
                return []
            lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            res = ['']
            for digit in digits:
                combine = lookup[digit]
                newres = []
                for char in combine:
                    for string in res:
                        newres.append(string+char)
                res = newres
            return res
    
    #if False:
    # DFS
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def dfs(digits, ind, path):
            if len(digits) == len(path):
                res.append(path)
                return 0
            else:
                for char in lookup[digits[ind]]:
                    dfs(digits, ind+1, path+char)
        dfs(digits, 0, '')
        return res 
