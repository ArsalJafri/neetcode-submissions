class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, nums in enumerate(nums):
            different = target - nums # 7 - 3 
            if different in hashmap:
                return [hashmap[different], i]
            hashmap[nums] = i

            