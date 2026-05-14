class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #so the solution is to iterate thru the list for nums.
        #and then we use a 2 pointer method to check if l + r + num = 0
        #shouldnt be that hard i hope

        nums.sort()
        out = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]
                
                if threeSum > 0: #The sum is too big. move the right pointer in.
                    r -= 1
                elif threeSum < 0: #The sum is too small. move the left pointer in.
                    l += 1
                else: #The sum is 0. Append solution.
                    out.append([n, nums[l], nums[r]])
                    l += 1
                    #then, move the left pointer in to a unique number.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                

        return out