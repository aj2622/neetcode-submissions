from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        @cache
        def dp(n, first_robbed):
            if n >= len(nums):
                return 0
            if n == len(nums)-1:
                if first_robbed:
                    return 0
                else:
                    return nums[-1]
            return max(nums[n]+dp(n+2,first_robbed), dp(n+1,first_robbed))
        
        return max(nums[0]+dp(2,True), dp(1,False))