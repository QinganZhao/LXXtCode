class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1:
            return True
        for diff in range(-len(matrix), len(matrix[0])):
            checker = 0
            for i in range(len(matrix)):
                if i + diff >= 0 and i + diff < len(matrix[0]):
                    if not checker:
                        checker = 1
                        val = matrix[i][i+diff]
                    else:
                        if matrix[i][i+diff] != val:
                            return False
        return True
