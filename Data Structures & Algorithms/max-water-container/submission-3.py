class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        answer = 0

        while left < right:
            if heights[left] <= heights[right]:
                small = heights[left]
                total = small * (right - left)
                left +=1 
            else:
                small = heights[right]
                total = small * (right - left)
                right -=1  
            
            answer = max(answer, total)
        
        return answer