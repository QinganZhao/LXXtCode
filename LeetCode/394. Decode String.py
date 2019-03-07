class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                num = ''
                while stack and stack[-1] in '0123456789':
                    num = stack.pop() + num
                string *= int(num)
                stack.append(string)
        return ''.join(stack)
