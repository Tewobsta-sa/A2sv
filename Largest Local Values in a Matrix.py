class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                submatrix = [
                    grid[i + r][j + c]
                    for r in range(3)
                    for c in range(3)
                ]
                max_local[i][j] = max(submatrix)

        return max_local
