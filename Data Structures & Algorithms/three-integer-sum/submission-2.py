class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        nums.sort()

        for i in range(0,len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1

        return [list(element) for element in ans]