### Naive way (TLE)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        current = [0, 0]
        currentDirect = [0, 1]
        for command in commands:
            if command == -1 or command == -2:
                currentDirect = self.turn(currentDirect, command)
            else:
                Next = [current[i] + currentDirect[i]*command for i in range(2)]
                if current[0] == Next[0]:
                    index = 0
                else:
                    index = 1
                obs = sorted([ob for ob in obstacles if ob[index] == current[index] and ob[1-index] in range(min(current[1-index], Next[1-index])+(sum(currentDirect)==1), max(current[1-index], Next[1-index])-(sum(currentDirect)==-1)+1)], key=lambda x: x[1-index], reverse = sum(currentDirect)-1)
                if obs :
                    Next[1-index] = obs[0][1-index] - sum(currentDirect)
                current = Next
        return current[0] ** 2 + current[1] ** 2
    
            
    def turn(self, currentDirect, command):
        if command == -1:
            if currentDirect == [1, 0]:
                return [0, -1]
            if currentDirect == [-1, 0]:
                return [0, 1]
            if currentDirect == [0, 1]:
                return [1, 0]
            if currentDirect == [0, -1]:
                return [-1, 0]
        if command == -2:
            if currentDirect == [1, 0]:
                return [0, 1]
            if currentDirect == [-1, 0]:
                return [0, -1]
            if currentDirect == [0, 1]:
                return [-1, 0]
            if currentDirect == [0, -1]:
                return [1, 0]
            
### Smarter way
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        currentX = currentY = d = res = 0
        obstacles = set(map(tuple, obstacles))
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for command in commands:
            if command == -2:
                d = (d - 1) % 4
            elif command == -1:
                d = (d + 1) % 4
            else:
                x, y = directions[d]
                while command and (currentX+x, currentY+y) not in obstacles:
                    currentX += x
                    currentY += y
                    command -= 1
            res = max(res, currentX ** 2 + currentY ** 2)
        return res    
