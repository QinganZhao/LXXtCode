class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = float('-inf')
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.max:
            self.max = x

    def pop(self) -> int:
        res = self.stack.pop()
        if res == self.max:
            if self.stack:
                self.max = max(self.stack)
            else:
                self.max = float('-inf')
        return res
    
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        newStack = []
        while self.stack:
            current = self.stack.pop()
            if current == self.max:
                res = current
                self.max = float('-inf')
            else:
                newStack = [current] + newStack
        if newStack:
            self.stack = newStack
            self.max = max(newStack)
        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
