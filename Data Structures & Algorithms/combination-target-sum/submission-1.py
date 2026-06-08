class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(start, path):
            if sum(path) == target:
                ans.append(path)
                return

            for i in range(start, len(nums)):
                if sum(path + [nums[i]]) > target:
                    break
                backtrack(i, path + [nums[i]])
        
        backtrack(0, [])

        return ans