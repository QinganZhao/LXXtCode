class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque()
        self.size = 0
 
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.size += 1
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        queue = collections.deque()
        size = self.size
        while size > 1: 
            queue.append(self.stack.popleft())
            size -= 1
        res = self.stack.popleft()
        self.stack = queue
        self.size -= 1
        return res

    def top(self) -> int:
        """
        Get the top element.
        """ 
        queue = collections.deque()
        size = self.size
        while size:
            if size == 1:
                res = self.stack.popleft()
                queue.append(res)
            else:
                queue.append(self.stack.popleft())
            size -= 1
        self.stack = queue
        return res
    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.size:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
