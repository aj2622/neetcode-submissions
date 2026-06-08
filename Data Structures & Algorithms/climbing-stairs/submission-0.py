from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # top down
        @cache
        def dp(state):
            # dp(state) - number of distinct ways to climb stairs of length state
            # base case
            if state == 0:
                return 0
            if state == 1:
                return 1
            if state == 2:
                return 2
            return dp(state-1) + dp(state-2)

        return dp(n)