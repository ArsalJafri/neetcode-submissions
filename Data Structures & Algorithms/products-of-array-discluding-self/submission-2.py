class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #two pass algo
        #prefix and suffix
        #fancy way of building from the left 
        #and multipying from the right
        prefix = []
        product = 1
        for i in range(len(nums)):
            prefix.append(product)
            product = nums[i] * product

        rightSide = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= rightSide
            rightSide = nums[i] * rightSide
        return prefix


