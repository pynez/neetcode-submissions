class Solution:
    def trap(self, height: List[int]) -> int:
        #i think the solution for this would be to use 2 pointers.
        #when we encounter a bar with our left pointer, we use the right pointer
        #to check for another bar, where the height of the bar has to be >= left pointer bar
        #we have an ongoing sum we add to.

        '''
        for example: Input: height = [0,2,0,3,1,0,1,3,2,1]
        l = 0, thats not a bar. l += 1
        l = 2, thats a bar. define r as l + 1
        set tentative area to 0.
        r = 0, thats not a bar. add l-r = 2-0 to tentative area
        r = 3, thats a bar, and r >= l. add tentative area to sum.
        

        now, l = r and r = r + 1
        keep going until r is at the end.
        '''
        total_area = 0
        l = 0
        r = l
        while (l < len(height) - 1): #loop til last index
            while height[l] == 0:
                l += 1

            r = l + 1
            print(f"left bar found at l = {l}")
            area = 0
            while(r < len(height) - 1 and height[r] < height[l]):
                print(f"no right bar found. adding {height[l] - height[r]} to tentative")
                area += height[l] - height[r]
                r += 1
            if height[r] >= height[l]:
                print(f"right bar found at r = {r}")
                print(f"added {area} to {total_area}")
                total_area += area
                print(f"total area is now {total_area}")
                l = r
            else:
                print("no valid right bar found. incrementing l")
                l += 1

        return total_area