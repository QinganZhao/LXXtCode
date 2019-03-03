# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

### recursion
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0
        self.helper(nestedList, 1)
        return self.res
        
    def helper(self, nestedList, depth):
        if not nestedList:
            return
        res = []
        for i in nestedList:
            if i.isInteger():
                self.res += depth * i.getInteger()
            else:
                res.extend(i.getList())
        return self.helper(res, depth + 1)
    
### iteration
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        stack = []
        for i in nestedList:
            stack.append((i, 1))
        while stack:
            current, depth = stack.pop()
            if current.isInteger():
                res += depth * current.getInteger()
            else:
                for i in current.getList():
                    stack.append((i, depth+1))
        return res
