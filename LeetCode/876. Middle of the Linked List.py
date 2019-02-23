# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        index = 0
        while current:
            current = current.next
            index += 1
        i = 0
        current = head
        while current:
            if i == int(index/2):
                return current
            i += 1
            current = current.next
