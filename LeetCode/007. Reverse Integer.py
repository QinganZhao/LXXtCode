class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        String = str(x)
        length = len(String)
        if String[0] == '-':
            length -= 1
            String = String.replace('-', '')
        strings = []
        for i in range(length):
            strings += [String[i]]
        result = 0

        for i in range(len(strings)):
            result += int(strings[i]) * (10 ** i)
        if result < -2**31 or result > 2**31-1:
            return 0
        if x>= 0:
            return result
        else:
            return -result

