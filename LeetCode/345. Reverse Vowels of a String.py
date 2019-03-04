class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u',
                      'A', 'E', 'I', 'O', 'U'])
        stack, res = [], []
        for char in s:
            if char in vowels:
                stack.append(char)
        for char in s:
            if char in vowels:
                res.append(stack.pop())
            else:
                res.append(char)
        return ''.join(res)
