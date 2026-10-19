class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        max_area = 0
        right = len(heights) -1
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            cur_area = w*h
            max_area = max(max_area, cur_area)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_area
            