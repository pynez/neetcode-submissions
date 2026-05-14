class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #a brute force solution would be to find the area of every single possible container.

        #we can use a 2 pointer approach where we calculate the are using l and r bar
        #whichever bar is lower we move in and calculate the area again

        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r]) #calculate area
            if area > max_area:
                max_area = area

            #next we decide which pointer to move in
            if heights[l] > heights[r]: #if the left bar is bigger, we move in the right bar
                r -= 1
            else: #otherwise, we move in the left bar
                l += 1
        return max_area
            