class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(len(bin(n))):
            if 1<<i & n:
                count += 1
        return count