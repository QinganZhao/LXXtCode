# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = dummy = ListNode(0)
        digit = 0
        num = 0
        while l1 or l2:
            num = digit
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            digit, num = divmod(num, 10)
            result.next = ListNode(num)
            result = result.next
        if digit == 1:
            result.next = ListNode(1)
        return dummy.next
