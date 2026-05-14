class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in seen) and (i != seen.index(complement)):
                return [seen.index(complement), i]
            else:
                seen.append(nums[i])
