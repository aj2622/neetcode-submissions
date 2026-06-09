class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArraySum = nums[0]
        start, stop = 0, 0

        # window always = 1
        # increase window when it positive
        # decrease window when it negative
        while stop < len(nums):
            if start == stop: 
                stop += 1
            elif sum(nums[start:stop]) > 0:
                stop += 1
                maxSubArraySum = max(maxSubArraySum, sum(nums[start:stop]))
            elif sum(nums[start:stop]) <= 0:
                start +=1 
        while start < stop:
            maxSubArraySum = max(maxSubArraySum, sum(nums[start:stop]))
            start += 1
        return maxSubArraySum