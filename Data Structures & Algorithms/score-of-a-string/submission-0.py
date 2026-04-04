class Solution:
    def scoreOfString(self, s: str) -> int:
        total_sum = 0

        left = 0
        right = 1
        while right < len(s):
            total_sum += abs(ord(s[left]) - ord(s[right]))
            left += 1
            right += 1
        
        return total_sum