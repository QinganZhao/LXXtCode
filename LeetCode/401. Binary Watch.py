class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        watch = []
        self.hourMap = [2 ** i for i in range(4)]
        self.minuteMap = [2** i for i in range(6)]
        if num == 0:
            return ["0:00"]
        else:
            watch = self.watchStatus(num)
        
        return [i for i in list(map(self.watch2Time, watch)) if i is not None]
    
    def watchStatus(self, num):
        if num == 0:
            return [[0] * 10]
        else:
            prev = self.watchStatus(num - 1)
            res = []
            for state in prev:
                for i, digit in enumerate(state):
                    if state[i] != 1:
                        state[i] = 1
                        if state not in res:
                            res.append(state.copy())
                        state[i] = 0
            return res
        
    def watch2Time(self, watch):
        hour = sum([self.hourMap[i] * watch[i] for i in range(4)])
        minute = sum([self.minuteMap[i] * watch[i+4] for i in range(6)])
        if hour > 11 or minute > 59:
            return
        if minute < 10:
            minute = ':0' + str(minute)
        else:
            minute = ':' + str(minute)
            
        return str(hour) + minute
