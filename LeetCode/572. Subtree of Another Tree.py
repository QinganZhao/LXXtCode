# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### Compare node using list: O(st)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool: 
        sTreeList = []
        tTreeList = []
        stack = [s]
        while stack:
            current = stack.pop()
            if current:
                sTreeList.append(current.val)
                stack.extend([current.right, current.left])
            else:
                sTreeList.append('END')
        stack = [t]
        while stack:
            current = stack.pop()
            if current:
                tTreeList.append(current.val)
                stack.extend([current.right, current.left])
            else:
                tTreeList.append('END')
        for i, sub in enumerate(sTreeList):
            if sub == tTreeList[0]:
                for j in range(i, len(sTreeList)):
                    if tTreeList[j-i] != sTreeList[j]:
                        break
                    if j - i == len(tTreeList) - 1 and tTreeList[j-i] == sTreeList[j]:
                        return True
        return False          
