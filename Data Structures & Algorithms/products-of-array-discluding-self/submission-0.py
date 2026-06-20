class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [1]
        temp = 1
        for i in range(len(nums)):
            preprod.append(temp*nums[i])
            temp = preprod[-1]
        preprod = preprod[:-1]

        rev = nums[::-1]
        postprod = [1]
        temp = 1
        for i in range(len(rev)):
            postprod.append(temp*rev[i])
            temp = postprod[-1]
        postprod = postprod[:-1][::-1]

        return [preprod[i]*postprod[i] for i in range(len(nums))]