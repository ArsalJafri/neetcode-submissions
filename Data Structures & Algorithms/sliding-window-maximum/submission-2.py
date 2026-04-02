class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        answer = []
        left = [0] * len(nums)
        right = [0] * len(nums) 
        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(len(nums)):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i-1])

        for i in range(len(nums) - 1, -1, -1):
            if (i+1) % k == 0 or i == len(nums) - 1:
                right[i] = nums[i]
            else:
                right[i] = max(nums[i], right[i+1])

        for i in range(len(nums)-k+1):
            answer.append(max(right[i], left[i+k-1]))
        
        return answer
        


