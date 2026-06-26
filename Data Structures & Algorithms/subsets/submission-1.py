class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        def dfs(current, remaining):
            if not remaining: 
                ans.add(tuple(sorted(current)))

            while remaining:
                dfs(current + [remaining.pop()], remaining[:])
                dfs(current, remaining)

            # for idx, nxt in enumerate(remaining):
            #     dfs(current+[nxt], remaining[:idx]+remaining[idx+1:])
            #     dfs(current, remaining[:idx]+remaining[idx+1:])
        
        dfs([], nums)

        return [list(element) for element in ans]
