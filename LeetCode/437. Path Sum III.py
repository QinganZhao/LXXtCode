# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### brutal force
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
    
    def findPath(self, root, sum):
        if root:
            return int(root.val == sum) + self.findPath(root.left, sum - root.val) + self.findPath(root.right, sum - root.val)
        return 0
    
    
### optimized using hashmap
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        self.findPath(root, sum, 0, {0:1})
        return self.res
        
        
    def findPath(self, root, sum, sumCurrent, dic):
        if root:
            complement = sumCurrent + root.val - sum
            self.res += dic.get(complement, 0)
            dic[sumCurrent+root.val] = dic.get(sumCurrent+root.val, 0) + 1
            self.findPath(root.left, sum, sumCurrent+root.val, dic)
            self.findPath(root.right, sum, sumCurrent+root.val, dic)
            dic[sumCurrent+root.val] -= 1
            # because we don't want current sum in left side affect the right side
        return
