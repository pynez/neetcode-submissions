class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs = {}
        for i in range(len(nums)):
            if nums[i] in freqs:
                return True
            else:
                freqs[nums[i]] = 1
        return False


        
        