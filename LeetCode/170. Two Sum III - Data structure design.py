class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.nums:
            self.nums[number] = 1
        else:
            self.nums[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums:
            if self.nums.get(value - num):
                if self.nums[value - num] == 1 and value == num * 2:
                    continue
                return True
        return False
            

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
