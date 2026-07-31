class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap for number frequencies, then find the k most
        #frequent elements by iteratiing through the hashmap.

        freqs = {}
        inverted_freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            else:
                freqs[num] += 1

        for num in freqs:
            if freqs[num] not in inverted_freqs:
                inverted_freqs[freqs[num]] = num

        count = 0
        out = []

        while count < k:
            maxFreq = max(inverted_freqs.keys())
            out.append(inverted_freqs[maxFreq])
            inverted_freqs.pop(maxFreq)
            count += 1

        return out

        