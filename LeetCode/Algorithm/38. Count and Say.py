class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        if n == 1:
            return res
        for _ in range(2, n+1):
            count, num, pos = [0], [res[0]], 0
            for j in res:
                if j != num[-1]:
                    num += [j]
                    count += [0]
                    pos += 1
                count[pos] += 1
            reslist = [(str(count[i]) + num[i]) for i in range(pos+1)]
            res = ''.join(reslist).replace('0', '')
        return res        
