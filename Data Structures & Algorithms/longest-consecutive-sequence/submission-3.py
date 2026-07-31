class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we should only consider numbers that can be the start
        # of a sequence. when we encounter a number in the list,
        # if num - 1 exists in the list, we don't have to consider
        # num.
    
        sequences = [0] * len(nums)
        numsDict = dict(zip(nums, sequences))
        for num in nums:
            if not (num - 1 in numsDict):
                numsDict[num] = 1
                nextNum = num + 1
                while nextNum in numsDict:
                    numsDict[num] += 1
                    nextNum += 1

        return max(numsDict.values())
