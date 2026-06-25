import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distOrigin(x,y):
            return math.sqrt(x**2+y**2)
        
        heap = []

        for point in points:
            x,y = point
            dist = distOrigin(x,y)
            heapq.heappush(heap, (dist,(x,y)))
        
        ans = []
        for _ in range(k):
            dist, (x, y) = heapq.heappop(heap)
            ans.append([x,y])

        return ans