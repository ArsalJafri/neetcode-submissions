class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        difference = 0
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                difference = target - nums[i]
                return [hashmap[difference], i]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i # 3 0
            
            
