class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
         # Get the number of rows and columns in the matrix
        rows = len(matrix)
        columns = len(matrix[0])

        # Create a new matrix with swapped dimensions
        transposed = [[0 for _ in range(rows)] for _ in range(columns)]

        # Fill in the transposed matrix
        for i in range(rows):
            for j in range(columns):
                transposed[j][i] = matrix[i][j]

        return transposed
