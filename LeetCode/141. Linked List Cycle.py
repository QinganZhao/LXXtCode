# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        seen = []
        while current:
            if current in seen:
                return True
            seen.append(current)
            current = current.next
        return False
