class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        dictionary = {}
        left = 0
        answer = 0

        for right in range(len(s)):
            if s[right] in dictionary:
                left = max(dictionary[s[right]] + 1,  left)

            dictionary[s[right]] = right
            answer = max(answer, right - left + 1)
        
        return answer


                





            


        