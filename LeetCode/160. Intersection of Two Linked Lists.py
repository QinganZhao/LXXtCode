# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return 
        currentA = headA
        currentB = headB
        aSeen = []
        while currentA:
            aSeen.append(currentA)
            currentA = currentA.next
        while currentB:
            if currentB in aSeen:
                return currentB
            currentB = currentB.next
        return
