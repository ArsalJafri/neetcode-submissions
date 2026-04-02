
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for i in range(len(s)):
           if s[i] in counts.keys():
             counts[s[i]] += 1
           else:
            counts[s[i]] = 1
           if t[i] in counts.keys():
            counts[t[i]] -= 1
           else:
            counts[t[i]] = -1
        
        for values in counts.values():
            if values != 0:
                return False
            
        return True  

