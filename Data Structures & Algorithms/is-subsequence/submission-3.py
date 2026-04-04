class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True 

        left = 0 #keeps track of t
        right = 0 # keeps track of s

        while left < len(t): 
            if t[left] == s[right]: #we found a match!
                left += 1
                right += 1
            else:
                left += 1 # keep t moving
            if right > len(s):
                return False
            if right == len(s):
                break

        if right < len(s):
            return False 
        if len(s) == right:
            return True
            
        