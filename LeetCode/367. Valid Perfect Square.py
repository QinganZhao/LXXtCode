### Newton's Method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        fac = num
        while fac * fac > num:
            fac = (fac + num / fac) // 2
        return fac * fac == num
    

### 1+3+5+... trick
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return not num       
