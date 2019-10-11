"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {i.id: i for i in employees}
        return self.dfs(dic, id)
    
    def dfs(self, dic, id):
        return dic[id].importance + sum([self.dfs(dic, i) for i in dic[id].subordinates])
