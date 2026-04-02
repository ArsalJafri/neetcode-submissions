class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []

        nums.sort()
       

        for i in range(len(nums)- 1):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            left = i + 1  
            right = len(nums) - 1

            while left < right:

                if nums[left] + nums[right] + nums[i] == 0:
                    arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1


                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                    if nums[left] == nums[left - 1]:
                        continue
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                    if nums[right] == nums[right + 1]:
                        continue
                
                
                
        
        return arr
