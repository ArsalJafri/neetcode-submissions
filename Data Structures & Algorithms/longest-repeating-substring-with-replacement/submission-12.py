class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        highest = 0

        hashmap = {}

        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1
            
            max_freq = max(hashmap.values())

            while (right - left + 1) - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
            
            highest = max(highest, (right -left +1))

        
        return highest 