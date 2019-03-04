class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.val = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.val) == self.size:
            self.val.pop(0)
        self.val.append(val)
        return sum(self.val) / len(self.val)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
