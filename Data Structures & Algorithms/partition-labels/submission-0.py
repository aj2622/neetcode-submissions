from collections import *

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        ans = []

        dic = {}
        for idx, char in enumerate(s):
            dic[char] = idx
        
        start, end = 0, 0

        while start < len(s):
            _start = start
            end = dic[s[start]]
            while start <= end:
                end = max(end, dic[s[start]])
                start += 1
            ans.append(end-_start+1)
        return ans