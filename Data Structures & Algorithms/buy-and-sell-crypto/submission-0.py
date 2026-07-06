class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices = [101] + prices

        i,j = 0,0
        n = len(prices)
        ans = 0

        for j in range(1,n):

            while prices[j] - prices[i] < 0:
                i += 1
            ans = max(ans, prices[j] - prices[i])
        return ans
