class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        i, j = 0, 0
        ans = 0
        counter = Counter('')
        while j < len(s):
            counter[s[j]] += 1
            j += 1
            if counter.total()-counter.most_common(1)[0][1] > k:
                counter[s[i]] -= 1
                i += 1
            ans = max(ans, j-i)
        return ans

        