"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}
        dont_visit = set()

        def dfs(node):
            dont_visit.add(node)
            # once a node is visited you create its copy
            if not node in seen:
                copy = Node(node.val, [])
                seen[node] = copy

            for nxt in node.neighbors:

                # neighbor exists
                if nxt in seen:
                    pass
                # neighbor does not exist
                if nxt not in seen:
                    nxt_copy = Node(nxt.val, [])
                    seen[nxt] = nxt_copy
                seen[node].neighbors.append(seen[nxt])

                if nxt not in dont_visit:
                    dfs(nxt)
        
        dfs(node)

        return seen[node]
