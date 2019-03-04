class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        stack = list(S.replace('-', ''))
        i, res, strNum = 1, '', len(stack)
        while stack:
            res = stack.pop().upper() + res
            if not i % K and i != strNum:
                res = '-' + res
            i += 1
        return res
