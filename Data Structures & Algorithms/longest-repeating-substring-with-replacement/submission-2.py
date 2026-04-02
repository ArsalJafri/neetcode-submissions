class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        answer = 0

        left = 0
        maxFrequent = 0
        for right in range(len(s)):
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
            maxFrequent =  max(maxFrequent, dictionary[s[right]])

            while (right - left + 1) - maxFrequent > k:
                dictionary[s[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
           
        return answer
        
        

        

                