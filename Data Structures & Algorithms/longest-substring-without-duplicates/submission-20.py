class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        highest = 0
        arr = set()
        for i in range(len(s)):
            while s[i] in arr:
                arr.remove(s[left])
                left += 1
            
            arr.add(s[i])
            highest = max(highest, len(arr))
            

        return highest
        