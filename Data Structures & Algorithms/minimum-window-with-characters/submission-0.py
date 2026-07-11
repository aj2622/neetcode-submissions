class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i, j = 0, 0

        counter = Counter(t)
        uniq_t = set(t)
        ans = '1'*1001
        while j < len(s):
            if s[j] in uniq_t:
                counter[s[j]] -= 1
            j += 1
            while all(value <= 0 for key, value in counter.items()):
                ans = min(ans, s[i:j], key = lambda x : len(x))
                if s[i] in uniq_t:
                    counter[s[i]] += 1
                i += 1
        return ans if ans != '1'*1001 else ''