class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we use a hash set for O(1) membership lookups
        numsSet = set(nums)

        sequenceLengths = [1] * len(nums)
        for i in range(len(numsSet)):
            nextnum = True
            char = nums[i]
            while nextnum:
                if char + 1 in numsSet:
                    sequenceLengths[i] += 1
                    char += 1
                else:
                    nextnum = False

        return max(sequenceLengths)