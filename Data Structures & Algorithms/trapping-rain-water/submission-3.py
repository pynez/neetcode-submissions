class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        for this problem we want to do 2 passes of the array to store prefix and suffix maximums.
        we can use this information to do one final pass and calculate the
        amount of water at each index.
        '''

        prefix_maxes = [0] * len(height)
        suffix_maxes = [0] * len(height)
        
        
        preMax = sufMax = total = 0
        for i in range(len(height)):
            prefix_maxes[i] = preMax
            if height[i] > preMax:
                preMax = height[i]

        print(f"prefix maxes: {prefix_maxes}")
        

        for i in range(len(height)-1, 0, -1 ):
            suffix_maxes[i] = sufMax
            if height[i] > sufMax:
                sufMax = height[i]

        print(f"suffix maxes: {suffix_maxes}")
        for i, n in enumerate(height):
            water = min(prefix_maxes[i], suffix_maxes[i]) - n
            if water > 0:
                print(f"added {water} to total")
                total += water
                print(f"total is now {total}")
        return total
