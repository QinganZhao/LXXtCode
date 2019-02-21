class AutocompleteSystem:

    def __init__(self, sentences: 'List[str]', times: 'List[int]'):
        self.trie = Trie()
        self.sentences = sentences
        self.times = times
        self.inputs = ''
        sentencesWithTimes = list(zip(self.sentences, self.times))
        for i, sentenceWithTime in enumerate(sentencesWithTimes):
            self.trie.add(sentenceWithTime[0], sentenceWithTime[1])

    def input(self, c: 'str') -> 'List[str]':   
        if c != '#':
            self.inputs += c
            res = sorted(self.trie.search(self.inputs).items(), 
                         key=lambda x: (-x[1], x[0]))
            if not res:
                return []
            if len(res) <= 3:
                return list(zip(*res))[0]
            return list(zip(*res[:3]))[0]
        if c == '#':
            self.trie.add(self.inputs, 1)
            self.inputs = ''
            return []

        
class Trie:
    
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.sentenceIndex = {}
        
    def add(self, sentence, time):
        trie = self
        for char in sentence:
            trie = trie.children[char]
        if sentence in trie.sentenceIndex:
            time += trie.sentenceIndex[sentence]
        trie.sentenceIndex.update({sentence: time})
        
    def search(self, string):
        res = {}
        current = self
        for char in string:
            if char in current.children:
                current = current.children[char]
            else:
                return res
        stack = collections.deque([current])
        while stack:
            current = stack.pop()
            if current.sentenceIndex:
                for i in current.sentenceIndex:
                    if i not in res:
                        res[i] = 0
                    res.update({i : res[i] + current.sentenceIndex[i]})
            for child in current.children:
                stack.append(current.children[child])
        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
