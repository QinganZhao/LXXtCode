class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        prev = self.queue
        stack = []
        while prev:
            stack.append(prev.pop())
        self.queue = [x]
        while stack:
            self.queue.append(stack.pop())
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop() 

    def peek(self) -> int:
        """
        Get the front element.
        """
        res = self.queue.pop()
        self.queue.append(res)
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
