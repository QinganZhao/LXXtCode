class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack, Dict = [], {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in Dict:
                stack.append(i)
            elif len(stack) == 0 or Dict[stack.pop()] != i:
                return False
        return len(stack) == 0
