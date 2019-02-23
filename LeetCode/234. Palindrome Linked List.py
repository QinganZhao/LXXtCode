# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = head
        List = []
        stack = []
        while dummy:
            List.append(dummy.val)
            dummy = dummy.next
        while List:
            if List[0] == List.pop():
                if List:
                    List.pop(0)
            else:
                return False
        return True
