class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binList = list(str('{0:{fill}32b}'.format(n, fill='0')))
        reverseStr = ''
        while binList:
            reverseStr += binList.pop()
        return int(reverseStr, 2)`
