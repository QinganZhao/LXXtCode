class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i-j] += res[i-j-1]
        return res
