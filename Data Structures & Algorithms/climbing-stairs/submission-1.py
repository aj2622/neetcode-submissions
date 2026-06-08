from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # # top down
        # @cache
        # def dp(state):
        #     # dp(state) - number of distinct ways to climb stairs of length state
        #     # base case
        #     if state == 0 or state == 1 or state = 2:
        #         return state
        #     return dp(state-1) + dp(state-2)

        # return dp(n)

        # bottom up 
        if n == 1 or n == 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]