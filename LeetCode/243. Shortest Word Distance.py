class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1Index = res = float('inf')
        word2Index = float('-inf')
        for i, word in enumerate(words):
            if word == word1:
                word1Index = i
            elif word == word2:
                word2Index = i
            res = min(res, abs(word1Index - word2Index))
        return res      
