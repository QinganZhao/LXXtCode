class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for num in nums2:
            stack.append(num)
            while len(stack) >= 2:
                if stack[-1] > stack[-2]:
                    dic[stack[-2]] = stack[-1]
                    tmp = stack.pop()
                    stack.pop()
                    stack.append(tmp)
                else:
                    break
        return [dic.get(num, -1) for num in nums1]
    
### cleaned version
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)
        return [dic.get(num, -1) for num in nums1]
