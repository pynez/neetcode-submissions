class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we can use a 2 pointer approach with pointers l and r
        #we calculate the volume as min(heights[l], heights[r])
        #multiplied by r - l. compare if that is greater than volume
        #and move l in if heights[l] < heights[r], otherwise move
        #r in.

        max_volume = 0
        l, r = 0, len(heights) - 1

        while l < r:
            volume = (min(heights[l], heights[r])) * (r - l)
            
            if volume > max_volume:
                max_volume = volume

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return max_volume
