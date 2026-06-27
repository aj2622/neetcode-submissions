class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ans = 0

        def dfs(i,j):
            grid[i][j] = 0
            nonlocal l
            l += 1
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == 1:
                    dfs(ni,nj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    l = 0
                    dfs(i,j)
                    ans = max(ans, l)
        
        return ans
