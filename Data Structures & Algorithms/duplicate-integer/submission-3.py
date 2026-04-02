class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = 0;
        counter = 0;
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 0

        
            
        return False

    