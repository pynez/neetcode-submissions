class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # A brute force way to do this would be with a nested for loop.
        # For each number in nums, I'll go thru nums again
            # as long as the outer loop index doesnt match the
            #inner loop index, we can multiply base by inner loop
            #value. then, append base to out.

        out = []
        for i in range(len(nums)):
            base = 1
            for j in range(len(nums)):
                if not i == j:
                    base *= nums[j]
            out.append(base)

        return out