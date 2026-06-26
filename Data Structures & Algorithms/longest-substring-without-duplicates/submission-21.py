class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        belly = set()
        longest_streak = 0

        for right in range(len(s)):
            while s[right] in belly:
                belly.remove(s[left])
                left += 1
            
            belly.add(s[right])
            longest_streak = max(longest_streak, len(belly))

        
        return longest_streak