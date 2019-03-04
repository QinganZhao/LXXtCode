### brutal force (Memory Error)
class StringIterator:

    def __init__(self, compressedString: str):
        self.list = []
        numRange = range(ord('0'), ord('9')+1)
        stringList = list(compressedString)
        while stringList:
            char = stringList.pop(0)
            num = ''
            while stringList and ord(stringList[0]) in numRange:
                num += stringList.pop(0)
            self.list.extend([char] * int(num))
        
    def next(self) -> str:
        if self.list:
            return self.list.pop(0) 
        return ' '
    
    def hasNext(self) -> bool:
        if self.list:
            return True
        return False
    

### using numbers to do calculation rather than decompressing everything
class StringIterator:

    def __init__(self, compressedString: str):
        if not compressedString:
            self.list = []
        else:
            numRange = range(ord('0'), ord('9')+1)
            ### because the last char cannot be extracted
            stringList = list(compressedString)+['*']
            num, char = '', stringList.pop(0)
            self.list = []
            for i, ch in enumerate(stringList):
                if ord(ch) in numRange:
                    num += ch
                else:
                    self.list.append([char, int(num)])
                    char = ch
                    num = ''         

    def next(self) -> str:
        if not self.list:
            return ' '
        if self.list[0][-1] == 1:
            return self.list.pop(0)[0] 
        else:
            self.list[0][-1] -= 1
            return self.list[0][0]
    
    def hasNext(self) -> bool:
        if self.list:
            return True
        return False

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
