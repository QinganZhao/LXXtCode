class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Set = set()
        for i in nums:
            if i not in Set:
                Set.add(i)
            else:
                Set.remove(i)
        return list(Set)[0]
