class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 200

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1
                res = min(res, nums[mid])
                
        return res
