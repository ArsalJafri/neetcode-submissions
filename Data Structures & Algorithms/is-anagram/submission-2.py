class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 0
        
        hashmap2 = {}
        for i in range(len(t)):
            if t[i] in hashmap2:
                hashmap2[t[i]] += 1
            else:
                hashmap2[t[i]] = 0
        

        for key in hashmap.keys():
            if key not in hashmap2:
                return False
            if hashmap[key] != hashmap2[key]:
                return False

        return True


