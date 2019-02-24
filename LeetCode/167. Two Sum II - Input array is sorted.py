### binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            find = target - num
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == find:
                    return [i+1, mid+1]
                if numbers[mid] < find:
                    l = mid + 1
                else:
                    r = mid - 1
                    
### two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
                
### dictionary
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            dic[target-num] = i + 1
        for i, num in enumerate(numbers):
            if dic.get(num):
                return [i+1, dic[num]]  
