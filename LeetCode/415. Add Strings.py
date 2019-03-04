class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1List, num2List = list(num1), list(num2)
        carry, res = 0, ''
        while num1List and num2List:
            add = int(num1List.pop()) + int(num2List.pop()) + carry
            carry, add = add // 10, add % 10
            res = str(add) + res
        numList = num1List or num2List
        while numList:
            add = int(numList.pop()) + carry
            carry, add = add // 10, add % 10
            res = str(add) + res
        if carry:
            res = '1' + res
        return str(res)
