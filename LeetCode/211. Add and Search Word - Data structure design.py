class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(WordDictionary)
        self.isWord = False

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        current = self
        for ch in word:
            current = current.children[ch]
        current.isWord = True   

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        current = self
        self.check = False
        self.dfs(current, word)
        return self.check
        
    def dfs(self, current, word):
        if not word:
            if current.isWord:
                self.check = True
            return 
        if word[0] == '.':
            for i in current.children.values():
                self.dfs(i, word[1:])
        else:
            current = current.children.get(word[0])
            if current is None:
                return
            self.dfs(current, word[1:])
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
