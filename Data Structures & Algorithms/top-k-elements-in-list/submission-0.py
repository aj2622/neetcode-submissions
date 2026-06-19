from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        list = Counter(nums)
        list = sorted(list.items(), key = lambda x : -x[1])

        return [list[i][0] for i in range(k)]