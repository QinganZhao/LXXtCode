class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        Set, res = set(nums), []
        for i in range(1, len(nums)+1):
            if i not in Set:
                res.append(i)
        return res
