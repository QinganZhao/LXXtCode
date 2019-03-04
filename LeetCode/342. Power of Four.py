### regular approach
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 4:
                return False
            num //= 4
        return True
    
    
### method without recursion or iteration
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0 or num & num-1:
            return False
        return num % 3 == 1
