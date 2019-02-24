### naive apporach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroNum = 0
        i = 0
        while nums:
            if nums[i] == 0:
                nums.pop(i)
                zeroNum += 1
                i -= 1
            i += 1
            if i >= len(nums) - 1:
                break
        for i in range(zeroNum):
            nums.append(0)

            
### smarter approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                

### "cheat" approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)
