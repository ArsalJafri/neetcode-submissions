class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        answer = 0

        left = 0
        maxFrequent = 0
        for right in range(len(s)):
            if s[right] in dictionary:
                dictionary[s[right]] += 1
            else:
                dictionary[s[right]] = 1 
            maxFrequent =  max(maxFrequent, dictionary[s[right]])

            while (right - left + 1) - maxFrequent > k:
                dictionary[s[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
           
        return answer
        
        

        

                