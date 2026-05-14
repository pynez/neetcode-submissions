class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char) - ord("a")] += 1

            results[tuple(chars)].append(s)

        out = []
        for value in results:
            out.append(results[value])
        return out