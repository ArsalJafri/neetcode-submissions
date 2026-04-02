class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        arr = []

        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            left = i + 1
            right = len(nums)- 1

            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    arr.append([ nums[left], nums[right], nums[i] ])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                    
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                    
            
        
        return arr
                