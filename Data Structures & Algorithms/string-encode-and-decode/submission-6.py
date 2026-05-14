class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if strs == [""]:
            return "[""]"
        return 'ø'.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "[""]":
            return [""]
        return s.split('ø')
