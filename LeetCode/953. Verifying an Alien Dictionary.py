class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        self.dic = {}
        for i, char in enumerate(order):
            self.dic[char] = i
        for i in range(1, len(words)):
            if self.cmp(words[i], words[i-1]) == -1:
                return False
        return True
    
    def cmp(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if self.dic[word1[i]] > self.dic[word2[i]]:
                return 1
            if self.dic[word1[i]] < self.dic[word2[i]]:
                return -1
        if len(word1) > len(word2):
            return 1
        if len(word1) < len(word2):
            return -1
        return 0
