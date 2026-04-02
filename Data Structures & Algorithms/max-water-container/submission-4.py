class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_max = -1

        while left < right:
            current_max = max( current_max, (right - left) * min(heights[right], heights[left]) ) 

            if heights[right] > heights[left]:
                left +=1
            else:
                right -= 1
        
        return current_max