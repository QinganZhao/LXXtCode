class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1]:
            return False
        if len(bits) < 2 or not bits[-2]:
            return True
        return self.checkNot(bits[:-2])
        
    def checkNot(self, bits):
        i = 0
        while i < len(bits):
            if bits[i]:
                i += 2
            else:
                i += 1
            if i > len(bits):
                return True
        return False
