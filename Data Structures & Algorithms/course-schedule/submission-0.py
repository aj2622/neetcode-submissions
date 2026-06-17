from collections import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        
        queue = deque([idx for idx, value in enumerate(indeg) if value == 0]) 

        order = []
        while queue:

            current = queue.popleft()
            order.append(current)
            for next in graph[current]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    queue.append(next)
        
        return len(order) == numCourses

