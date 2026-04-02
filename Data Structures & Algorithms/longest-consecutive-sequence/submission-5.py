class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mySet = set(nums)
        answer = 0

        for x in nums:
            if x -1 not in mySet:
                 #why is this line needed?
                y = x + 1
                while y in mySet:
                    y += 1
                answer = max(answer, y-x)
        
        return answer
