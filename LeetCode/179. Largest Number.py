class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        res = ''.join(sorted(map(str, nums), key=mySort, reverse=True))
        return '0' if res[0] == '0' else res
        
class mySort(str):
    def __lt__(x, y):
        return x + y < y + x
