from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])

        pacific = [[0]*C for _ in range(R)]
        start = deque([(0,j) for j in range(len(heights[0]))] + [(i,0) for i in range(1,len(heights))])
        seen = set(start)
        while start:
            i,j = start.popleft()
            pacific[i][j] = 1
            for _i, _j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0<= i + _i < R and 0 <= j + _j < C and heights[i+_i][j+_j] >= heights[i][j]:
                    if (i+_i,j+_j) not in seen:
                        seen.add((i+_i,j+_j))
                        start.append((i+_i,j+_j))

        atlantic = [[0]*C for _ in range(R)] 
        start = deque([(R-1,j) for j in range(C)] + [(i,C-1) for i in range(R-1)])
        seen = set(start)
        while start:
            i,j = start.popleft()
            atlantic[i][j] = 1
            for _i, _j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0<= i + _i < R and 0 <= j + _j < C and heights[i+_i][j+_j] >= heights[i][j]:
                    if (i+_i,j+_j) not in seen:
                        seen.add((i+_i,j+_j))
                        start.append((i+_i,j+_j))
                        
        return [(i,j) for i in range(R) for j in range(C) if atlantic[i][j]==1 and pacific[i][j]==1]
            