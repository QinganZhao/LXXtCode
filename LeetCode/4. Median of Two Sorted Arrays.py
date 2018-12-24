class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        res = sorted(nums1 + nums2)
        if length % 2:
            return res[int((length-1)/2)]
        else:
            return (res[int(length/2-1)]+res[int(length/2)])/2
