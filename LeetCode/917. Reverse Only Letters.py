class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alpha = set([chr(i) for i in list(range(ord('a'), ord('z')+1)) +
                     list(range(ord('A'), ord('Z')+1))])
        words, res = [], list(S)
        for char in res:
            if char in alpha:
                words.append(char)
        for i in range(len(res)):
            if res[i] in alpha:
                res[i] = words.pop()
        return ''.join(res)
