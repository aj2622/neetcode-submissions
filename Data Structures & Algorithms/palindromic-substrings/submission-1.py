class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def check(s):
            return s == s[::-1]
        
        ans = 0

        for i in range(len(s)):

            start, end = i, i+1
            while 0 <= start <= len(s) and 0 <= end <= len(s):
                if check(s[start:end]):
                    # print(s[start:end])
                    ans += 1
                    start, end = start - 1, end  + 1
                else:
                    break
            start, end = i, i+2
            while 0 <= start <= len(s) and 0 <= end <= len(s):
                if check(s[start:end]):
                    # print(s[start:end])
                    ans += 1
                    start, end = start - 1, end  + 1
                else:
                    break
                    
        
        return ans 