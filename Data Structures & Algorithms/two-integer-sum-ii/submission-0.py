class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since numbers are sorted, we can use two pointers:
        # We place left and right pointers at the ends of the list
        # if the sum of l and r is greater than target, we can move
        # the right pointer in by one. if it's smaller, we can move
        # the left pointer in by one.

        l, r = 0, len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
            