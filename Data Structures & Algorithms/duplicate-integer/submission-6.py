class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        dictionary = {}

        for i in range(len(nums)):
            if nums[i] in dictionary:
                return True
            else:
                dictionary[nums[i]] = 1
                print(dictionary[nums[i]])

        return False