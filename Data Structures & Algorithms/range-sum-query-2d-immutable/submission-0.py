class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows, cols = len(self.matrix), len(self.matrix[0])
        sum = 0
        if 0 <= row1 < rows or 0 <= row2 < rows or 0 <= col1 < cols or 0 <= col2 < cols:
            for r in range(row1, row2+1):
                for c in range(col1, col2+1):
                    sum += self.matrix[r][c]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)