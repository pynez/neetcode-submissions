class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We all know how to do this using brute force. 

        #I'm gonna try to put all numbers and their indices into a hash map.
        #After, i'll iterate through nums and subtract nums[i] from target to find complement
        #if complement is in our hash map, we can return i and key associated with complement.
        #While doing this, ill have to check to make sure we don't add the same index twice.

        complements = {}
        for i in range(len(nums)):
            complements[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                if not (complements[complement] == i):
                    return [min(complements[complement], i), max(complements[complement], i)]
        