from collections import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(set)

        for idx, str in enumerate(strs):
            dic[frozenset(Counter(str).items())].add(idx)

        return [[strs[idx] for idx in val] for _, val in dic.items()]