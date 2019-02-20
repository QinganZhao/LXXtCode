class Solution:
    def palindromePairs(self, words: 'List[str]') -> 'List[List[int]]':
        trie = self.constructTrie(words)
        res = []
        for i, word in enumerate(words):
            otherHalves = self.getPalindromeWords(trie, word, i)
            res.extend([i, j] for j in otherHalves if i != j)
        return res
    
    def isPalidrome(self, word):
        if len(word) == 0 or len(word) == 1:
            return True
        return word[0] == word[-1] and self.isPalidrome(word[1:-1])
    
    def constructTrie(self, words):
        trie = Trie()
        for i, word in enumerate(words):
            trie.add(word, i)
        return trie
    
    def getPalindromeWords(self, trie, word, index):
        res = []
        while word:
            if trie.wordEnd >= 0:
                if self.isPalidrome(word):
                    res.append(trie.wordEnd)
            if word[0] not in trie.children:
                return res
            trie = trie.children[word[0]]
            word = word[1:]
        if trie.wordEnd >= 0:
            res.append(trie.wordEnd)
        res.extend(trie.selfPalindromeWord)
        return res
    
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.wordEnd = -1
        self.selfPalindromeWord = []

    def add(self, word, index):
        current = self
        for i, char in enumerate(reversed(word)):
            if Solution().isPalidrome(word[0:len(word)-i]):
                current.selfPalindromeWord.append(index)
            current = current.children[char]
        current.wordEnd = index
