class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1: # visited
                return 0

            grid[i][j] = -1
            peri = 0
            peri += dfs(i+1, j)
            peri += dfs(i-1, j)
            peri += dfs(i, j+1)
            peri += dfs(i, j-1)
            return peri

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)