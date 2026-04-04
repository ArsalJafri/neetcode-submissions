class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0
        right = 0

        while left < len(s) and right < len (t):
            if t[right] == s[left]:
                left += 1
                right += 1
            else:
                left += 1
            
        
        return len(t) - right