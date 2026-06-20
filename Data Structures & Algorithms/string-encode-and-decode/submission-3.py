class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s_ in strs:
            res.append(str(len(s_)))
            res.append("#")
            res.append(s_)
        return "".join(res)



    def decode(self, s: str) -> LiAst[str]:
        res = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i += 1
            l = int(l)
            if l:
                res.append(s[i+1:i+l+1])
            else:
                res.append("")
            i += l+1
            

        return res
