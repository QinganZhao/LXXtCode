# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        res = TreeNode(0)
        stack = [(t1, t2, res)]
        while stack:
            t1Current, t2Current, resCurrent = stack.pop()
            if t1Current:
                if t1Current.left: resCurrent.left = TreeNode(0)
                if t1Current.right: resCurrent.right = TreeNode(0)
            if t2Current:
                if t2Current.left: resCurrent.left = TreeNode(0)
                if t2Current.right: resCurrent.right = TreeNode(0)
            if t1Current and t2Current:
                resCurrent.val = t1Current.val + t2Current.val        
                stack.extend([(t1Current.right, t2Current.right, resCurrent.right),
                              (t1Current.left, t2Current.left, resCurrent.left)])
            elif t1Current and not t2Current:
                resCurrent.val = t1Current.val
                stack.extend([(t1Current.right, None, resCurrent.right), 
                              (t1Current.left, None, resCurrent.left)])
            elif t2Current and not t1Current: 
                resCurrent.val = t2Current.val
                stack.extend([(None, t2Current.right, resCurrent.right), 
                              (None, t2Current.left, resCurrent.left)])
            else:
                resCurrent = None
        return res  
