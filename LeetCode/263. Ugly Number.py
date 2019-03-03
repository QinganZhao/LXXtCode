class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num and not num % 2:
            num //= 2
        if num == 1:
            return True
        else:
            while num and not num % 3:
                num //= 3
            if num == 1:
                return True
            else:
                while num and not num % 5:
                    num //= 5
                    if num == 1:
                        return True
        return False      
