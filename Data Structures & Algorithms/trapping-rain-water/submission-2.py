class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        leftTotal = height[left]
        rightTotal = height[right]
        

        while left < right:
            if leftTotal <= rightTotal:
                left += 1
                leftTotal = max(leftTotal, height[left])
                answer += leftTotal - height[left]
            else:
                right -=1
                rightTotal = max(rightTotal, height[right])
                answer += rightTotal - height[right]


        return answer
