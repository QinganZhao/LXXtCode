class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j, dic, res = 0, 0, {}, []
        for char in p:
            dic[char] = dic.get(char, 0) + 1
        dicCopy = dict(dic)
        while j < len(s):
            if j - i == len(p):
                res.append(i)
                dicCopy[s[i]] += 1
                i += 1
            elif not dic.get(s[j]):
                j += 1
                i = j
                dicCopy = dict(dic)
            elif dicCopy.get(s[j]):
                dicCopy[s[j]] -= 1
                j += 1
            else:
                dicCopy[s[i]] += 1
                i += 1
        if j - i == len(p):
            res.append(i)
        return res
