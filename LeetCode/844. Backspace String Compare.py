class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.backspace(S) == self.backspace(T)
        
    def backspace(self, s):
        List = list(s)
        i = 0
        while List:
            if List[i] == '#':
                if i == 0:
                    List.pop(i)
                    i -= 1
                else:
                    List.pop(i)
                    List.pop(i-1)
                    i -= 2
            i += 1
            if i >= len(List):
                break
        return str(List)
