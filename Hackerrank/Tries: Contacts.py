from collections import defaultdict, deque

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isName = False

    def add(self, name):
        current = self
        for char in name:
            current = current.children[char]
        current.isName = True

    def find(self, name):
        current = self
        for char in name:
            if char not in current.children:
                return 0
            current = current.children[char]
        return self.dfs(current)
    
    def dfs(self, start):
        res = 0
        stack = deque([start])
        visited = set()
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            if current.isName:
                res += 1
            visited.add(current)
            for child in current.children:
                stack.append(current.children[child])
        return res

if __name__ == '__main__':
    trie = Trie()
    n = int(input())
    
    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            trie.add(contact)

        if op == 'find':
            print(trie.find(contact))
