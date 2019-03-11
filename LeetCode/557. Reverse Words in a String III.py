class Solution:
    def reverseWords(self, s: str) -> str:
        newWords = []
        words = s.split()
        for word in words:
            newWords.append(word[::-1])
        return ' '.join(newWords)
