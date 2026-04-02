class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        curr = 0

        while left < right:
            curr = max(curr, min(heights[left], heights[right]) * (right - left) )

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            elif heights[right] == heights[left]:
                left += 1
            
            
        
        return curr
        
        