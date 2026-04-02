class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        curr_long = 0
        hashmap = {}
    

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
                
            hashmap[s[right]] = right
            

            curr_long = max(curr_long, (right -left) +1)
        
        return curr_long


