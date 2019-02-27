class Solution:
    def calPoints(self, ops: List[str]) -> int:
        numRange = range(ord('0'), ord('9')+1)
        stack = []
        for op in ops:
            if len(op) > 1 or ord(op) in numRange:
                stack.append(int(op))
            if op == 'C' and stack:
                stack.pop()
            if op == 'D' and stack:
                stack.append(stack[-1] * 2)
            if op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
    
### cleaned version (since the input will always be valid)
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
