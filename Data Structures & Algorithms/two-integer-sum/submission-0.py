class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for idx, num in enumerate(nums):
            if num in dic:
                return sorted([idx, dic[num]])
            else:
                dic[target-num] = idx