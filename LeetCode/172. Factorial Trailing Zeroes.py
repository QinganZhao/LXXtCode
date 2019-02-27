### brutal force (TLE)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        string = reversed(str(self.factorial(n)))
        res = 0
        for i in string:
            if i == '0':
                res += 1
            else:
                break
        return res
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
        
### smart approach:
### since trailing zeros can by only generated by 2, 5,
### and number of 2 is way more than 5 in any scenarios (domination),
### we only need to find out in n!,
### how many numbers are divisible by 5,
### 5*5, 5*5*5, 5*5*5*5, ......
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n //= 5
            res += n
        return res