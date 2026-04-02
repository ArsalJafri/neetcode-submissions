class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap: hashmap[s[i]] += 1
            else: hashmap[s[i]] = 1

            if t[i] in hashmap: hashmap[t[i]] -= 1
            else:  hashmap[t[i]] = -1
        
        return all(values == 0 for values in hashmap.values()) 