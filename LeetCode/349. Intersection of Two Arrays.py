### search in set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        Set = set(nums1)
        for num in nums2:
            if num in Set:
                res.add(num)
        return list(res)
    
### pythonic set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
