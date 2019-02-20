class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        trie = {}
        for word in words:
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current['ok!'] = 'ok!'
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, trie, '')
        return list(self.res)
    
    def search(self, board, i, j, current, prev):
        if 'ok!' in current:
            self.res.add(prev)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in current:
            self.used[i][j] = True
            self.search(board, i-1, j, current[board[i][j]], 
                        prev + board[i][j])
            self.search(board, i+1, j, current[board[i][j]], 
                        prev + board[i][j])
            self.search(board, i, j-1, current[board[i][j]], 
                        prev + board[i][j])
            self.search(board, i, j+1, current[board[i][j]], 
                        prev + board[i][j])
            self.used[i][j] = False
