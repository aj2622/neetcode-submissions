class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        return chr(256).join(strs)


    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        return s.split(chr(256))