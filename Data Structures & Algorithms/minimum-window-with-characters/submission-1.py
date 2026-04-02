class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        dictionaryT = {}

        for character in range(len(t)):

            if t[character] in dictionaryT:
                dictionaryT[t[character]] += 1
            else:
                dictionaryT[t[character]] = 1

        dictionary = {}
        left = 0
        answer = (-1,-1)
        matched = 0
        answerLength = float('inf')


        for right in range(len(s)):
            if s[right] in t:
                dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
                if dictionary[s[right]] == dictionaryT[s[right]]:
                    matched += 1

                while matched == len(dictionaryT):
                    if (right - left +1) < answerLength:
                        answer = (left, right)
                        answerLength = right - left + 1 
                    if s[left] in dictionaryT:
                        dictionary[s[left]] -= 1
                        if dictionary[s[left]] < dictionaryT[s[left]]:
                            matched -= 1
                    left += 1
        
        left, right = answer
        return s[left:right+1] if answerLength != float('inf') else ""
            
            
           



            
