class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices, heights at these indices are increasing
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # use height 0 as a sentinel at the end to flush the stack
            current_height = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > current_height:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area