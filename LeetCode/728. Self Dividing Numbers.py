class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            if self.check(num):
                res.append(num)
        return res
        
    def check(self, num):
        numList = map(int, list(str(num)))
        for n in numList:
            if not n or num % n:
                return 0
        return 1
