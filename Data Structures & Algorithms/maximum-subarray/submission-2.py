class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        
        window_sum = 0
        for num in nums:
            if window_sum <= 0:
                window_sum = num
            elif window_sum > 0:
                ans = max(ans, window_sum)
                window_sum += num

        return max(ans, window_sum)
