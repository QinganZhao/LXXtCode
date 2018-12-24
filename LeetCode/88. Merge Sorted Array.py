class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for num1 in nums1:
            if not nums2:
                break
            if num1 >= nums2[0]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
                nums1.pop()
            i += 1
        if nums2:
            for j in range(len(nums2)):
                nums1.pop()
            nums1 += nums2
