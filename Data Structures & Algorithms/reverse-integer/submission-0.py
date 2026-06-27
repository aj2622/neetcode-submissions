class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if '-' in x:
            ans = '-' + x[1:][::-1]
        else:
            ans = x[::-1]
        result = int(ans)
        if not -2**31 <= result <= 2**31 - 1:
            return 0
        return result