### naive transformation
class Solution:
    def toLowerCase(self, str: str) -> str:
        upper = set([chr(i) for i in range(ord('A'), ord('Z')+1)])
        diff = ord('A') - ord('a')
        res = ''
        for char in str:
            if char in upper:
                res += chr(ord(char) - diff)
            else:
                res += char
        return res
    
### Pythonic cheating
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
