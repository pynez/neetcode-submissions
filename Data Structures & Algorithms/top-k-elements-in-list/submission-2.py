class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 0

        def getFrequentKey(frequencies):
            maxKey = max(frequencies, key=frequencies.get)
            frequencies.pop(maxKey)
            return maxKey

        out = []
        for i in range(k):
            out.append(getFrequentKey(frequencies))

        return out
    

        