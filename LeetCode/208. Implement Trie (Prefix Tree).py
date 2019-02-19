class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(Trie)
        self.isWord = False

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        current = self
        for ch in word:
            current = current.children[ch]
        current.isWord = True
        
    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        current = self
        for ch in word:
            current = current.children.get(ch)
            if current is None:
                return False
        return current.isWord

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self
        for ch in prefix:
            current = current.children.get(ch)
            if current is None: 
                return False
        return True
