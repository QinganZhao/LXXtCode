class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not needle:
            return 0
        if not haystack:
            return -1
        cmp = haystack.split(needle)
        if cmp[0] == haystack:
            return -1
        else:
            return len(cmp[0])
