class Solution:
    
    # Built-in function
    '''
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
    '''
    
    # Think binary as decimal way
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        """
        res, i, j, c = '', len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >=0 or c:
            current = (i >= 0 and int(a[i])) + (j >= 0 and int(b[j]))
            c, current = divmod(current + c, 2)
            res = str(current) + res
            i -= 1
            j -= 1
        return res
            
            
