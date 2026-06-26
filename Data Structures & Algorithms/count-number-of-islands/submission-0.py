class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        ans = 0

        def dfs(i,j):
            seen.add((i,j))
            for _i, _j in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0<=_i<len(grid) and 0<=_j<len(grid[0]):
                    if (_i, _j) not in seen and grid[_i][_j]=='1':
                        dfs(_i, _j)
        
        start = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1']

        for i, j in start:
            if (i,j) not in seen:
                dfs(i,j)
                ans += 1

        return ans