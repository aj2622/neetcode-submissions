class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0


        def dfs(i, j):
            grid[i][j] = '0'
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]=='1':
                    dfs(ni,nj)

        




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1

        return ans