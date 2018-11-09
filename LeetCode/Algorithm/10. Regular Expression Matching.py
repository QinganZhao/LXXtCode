class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if re.match('^'+p+'$', s):
            return True
        else:
            return False
