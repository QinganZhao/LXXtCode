class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        res = 0
        for i in list(str(num)):
            res += int(i)
        return self.addDigits(res) 
