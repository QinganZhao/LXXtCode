class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        restNode = numCourses
        edge = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for end, start in prerequisites:
            edge[start].append(end)
            indegree[end] += 1
        stack = [] 
        for i in range(numCourses):
                if not indegree[i]:
                    stack.append(i)
        while stack:
            current = stack.pop()
            res.append(current)
            restNode -= 1
            for end in edge[current]:
                indegree[end] -= 1
                if not indegree[end]:
                    stack.append(end)
        if restNode:
            return []
        return res
