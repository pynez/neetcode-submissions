class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return "ø".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('ø')
