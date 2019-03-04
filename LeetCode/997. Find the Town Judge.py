class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:     
        judge, people = [], {}
        for i in trust:
            people[i[0]] = people.get(i[0], []) + [i[1]]
        for i in range(1, N+1):
            if i not in people:
                judge.append(i)
        if len(judge) != 1:
            return -1
        for i in people.values():
            if judge[0] not in i:
                return -1
        return judge[0]
