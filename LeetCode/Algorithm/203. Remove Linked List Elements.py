# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        current = dummy = ListNode(-1)
        dummy.next = head 
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
            
        return dummy.next
            
