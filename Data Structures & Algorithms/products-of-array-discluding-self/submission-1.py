class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # A brute force way to do this would be with a nested for loop.
        # For each number in nums, I'll go thru nums again
            # as long as the outer loop index doesnt match the
            #inner loop index, we can multiply base by inner loop
            #value. then, append base to out.

        # out = []
        # for i in range(len(nums)):
        #     base = 1
        #     for j in range(len(nums)):
        #         if not i == j:
        #             base *= nums[j]
        #     out.append(base)

        # return out

        # the identified bottleneck is the nested for loop.
        # this leads to a bunch of repeated calculations
        # which blows our time complexity up to O(n^2)

        # using hints i developed the following solution:
        # we use a two pass approach to fill prefix and suffix 
        # products for each index. then we iterate thru nums
        # and for each number, multiply it by its prefix and suffix

        out = []
        # find prefix products
        prefix = 1
        prefixes = []

        for i in range(len(nums)):
            prefixes.append(prefix)
            prefix *= nums[i]

        #find suffix products
        suffix = 1
        suffixes = []

        for i in reversed(range(len(nums))):
            suffixes.append(suffix)
            suffix *= nums[i]
            
        suffixes.reverse()
        # final pass to fill out
        for i in range(len(nums)):
            out.append(prefixes[i]*suffixes[i])

        return out
