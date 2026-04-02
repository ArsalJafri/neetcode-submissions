class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        #left pass
        leftProduct = 1
        for i in range(len(nums)):
            result[i] *= leftProduct
            leftProduct *= nums[i]
         
         #right pass
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightProduct
            rightProduct *= nums[i] 

        return result        
        