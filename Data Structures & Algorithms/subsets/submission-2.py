class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(current, remaining):
            if not remaining: 
                ans.append(current)

            while remaining:
                dfs(current + [remaining.pop()], remaining[:])
                dfs(current, remaining)
        
        dfs([], nums)

        return ans
