class Solution:
    def isHappy(self, n: int) -> bool:
        self.Seen = collections.defaultdict(int)
        return self.checker(n)
        
    def checker(self, n):
        self.Seen[n] = 1
        if n == 1:
            return True
        Sum = 0
        for i in str(n):
            Sum += int(i) ** 2
        if self.Seen[Sum]:
            return False
        return self.checker(Sum)
