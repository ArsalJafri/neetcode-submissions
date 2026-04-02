class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()

        for value in nums:
            if value not in arr:
                arr.add(value)
            else:
                return True
        
        return False