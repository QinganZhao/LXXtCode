### Topological Sort (BFS)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [[] for i in range(numCourses)]
        numPreq = [0] * numCourses 
        for course, preq in prerequisites:
            preqs[preq].append(course)
            numPreq[course] += 1
        queue = collections.deque()
        for i in range(numCourses):
                if not numPreq[i]:
                    queue.append(i)
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for course in preqs[current]:
                numPreq[course] -= 1
                if not numPreq[course]:
                    queue.append(course)
        return count == numCourses      
    
    
### Kahn's algorithm find whether the graph contains a cycle
### (DFS, also can be considered as Topological Sort) 
### basically only changed queue to stack... fuck
### have been thinking about this shit for whole night
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            restNode -= 1
            for end in edge[current]:
                indegree[end] -= 1
                if not indegree[end]:
                    stack.append(end)
        return not restNode
