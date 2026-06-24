class Solution:
    def trap(self, heights: List[int]) -> int:
        
        pre_max = [0]
        mx = 0
        for height in heights[:-1]:
            mx = max(mx, height)
            pre_max.append(mx)
        
        post_max = [0]
        mx = 0
        for height in heights[::-1][:-1]:
            mx = max(mx, height)
            post_max.append(mx)
        post_max = post_max[::-1]

        ans = 0
        for idx, height in enumerate(heights):
            ans += max(0, min(post_max[idx],pre_max[idx])-height)

        return ans