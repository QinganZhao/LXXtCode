class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned, punc = set(banned), set(['!', '?', "'", ',', ';', '.'])
        charList, dic = list(paragraph), {}
        for i, char in enumerate(charList):
            if char in punc:
                charList[i] = ' '
        paragraph = ''.join(charList).lower()
        words = paragraph.split()
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        rank = sorted(dic.items(), key = lambda x: x[1])
        while rank:
            if rank[-1][0] in banned:
                rank.pop()
            else:
                return rank[-1][0]
