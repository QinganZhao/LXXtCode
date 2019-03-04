class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('*')
        num = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                num += 1
            else:
                j = i - 1
                numList = list(str(num+1))
                num = 0
                if numList == ['1']:
                    numList = [] 
                while numList:
                    chars[j] = int(numList.pop())
                    j -= 1
                string = []
        i, j = 1, len(chars)
        while i < j:
            if type(chars[i]) != int and chars[i] == chars[i-1]:
                chars.pop(i)
                j -= 1
            else:
                i += 1
        for i in range(len(chars)):
            if type(chars[i]) == int:
                chars[i] = str(chars[i])
        chars.pop()
