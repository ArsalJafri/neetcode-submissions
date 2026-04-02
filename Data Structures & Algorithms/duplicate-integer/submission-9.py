class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()

        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.add(nums[i])
            else:
                return True
        
        return False