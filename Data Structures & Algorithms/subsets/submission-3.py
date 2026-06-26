class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        for i in range(1<<len(nums)):
            ans.append([nums[idx] for idx in range(len(nums)) if (i & 1<<idx)])

        return ans
