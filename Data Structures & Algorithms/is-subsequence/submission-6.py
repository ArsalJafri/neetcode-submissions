class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0 #keeps track of t
        right = 0 # keeps track of s

        while left < len(t) and right < len(s): 
            if t[left] == s[right]: #we found a match!
                left += 1
                right += 1
            else:
                left += 1 # keep t moving

        return right == len(s)
        