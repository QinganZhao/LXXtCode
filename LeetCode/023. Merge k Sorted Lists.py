# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        if not heap:
            return 
        res = dummy = ListNode(heapq.heappop(heap))
        for i in range(len(heap)):
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        return res
