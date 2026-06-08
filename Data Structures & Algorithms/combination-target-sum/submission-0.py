class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start, path):
            if sum(path) == target:
                ans.append(path)
                return
            if sum(path) > target:
                return

            for i in range(start, len(nums)):
                backtrack(i, path + [nums[i]])
        
        backtrack(0, [])

        return ans