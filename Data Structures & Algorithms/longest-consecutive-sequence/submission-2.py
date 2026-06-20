from collections import defaultdict, Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        parent = {num:num for num in nums}
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            parent[find(a)] = find(b)

        for num in nums:
            if num-1 in nums:
                union(num-1, num)
        
        source = Counter([find(num) for num in nums])
        

        return max(source.values(),default = 0)
