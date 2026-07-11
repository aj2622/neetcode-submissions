class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # Is the left half strictly sorted?
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1   # target in left sorted half
                else:
                    l = mid + 1   # target in right (possibly rotated) half
            else:
                # Otherwise the right half must be sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1   # target in right sorted half
                else:
                    r = mid - 1   # target in left (rotated) half
        return -1