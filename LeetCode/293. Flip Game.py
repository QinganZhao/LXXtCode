class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        strList = list(s)
        for i in range(len(s)-1):
            if strList[i] == '+' and strList[i+1] == '+':
                strList[i] = strList[i+1] = '-'
                res.append(''.join(strList))
                strList[i] = strList[i+1] = '+'
        return res
