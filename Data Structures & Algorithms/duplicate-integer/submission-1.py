class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                return True
            else:
                frequencies[num] = 1
        return False