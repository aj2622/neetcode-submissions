from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # max possible loot at index i
        @cache
        def dp(state):
            if state >= len(nums):
                return 0
            return max(nums[state]+dp(state+2), dp(state+1))


        return dp(0)
