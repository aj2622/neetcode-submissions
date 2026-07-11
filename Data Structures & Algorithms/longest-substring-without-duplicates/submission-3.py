from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1
        i, j = 0, 0
        ans = 0
        counter = Counter("")
        while j < len(s):
            if counter[s[j]] == 0:
                counter[s[j]] += 1
                j += 1
            else:
                counter[s[i]] -= 1
                i += 1
            ans = max(j-i, ans)
        return ans
