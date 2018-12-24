# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSym(root.left, root.right)
    
    def isSym(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
        return False
