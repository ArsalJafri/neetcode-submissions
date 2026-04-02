class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        deq = deque()
        left = 0

        for right in range(len(nums)):
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()

            deq.append(right)

            while deq[0] < left:
                deq.popleft()

            if (right + 1) >= k:
                output.append(nums[deq[0]])
                left += 1
            

        return output

      
        
        


