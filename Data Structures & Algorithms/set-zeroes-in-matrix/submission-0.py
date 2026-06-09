class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        r, c = len(matrix), len(matrix[0])

        def set_row_inf(r):
            for column in range(c):
                if matrix[r][column] != 0:
                    matrix[r][column] = float('inf')
        def set_col_inf(c):
            for row in range(r):
                if matrix[row][c] != 0:
                    matrix[row][c] = float('inf')
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    set_row_inf(i)
                    set_col_inf(j)
                    matrix[i][j] = float('inf')
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
        
