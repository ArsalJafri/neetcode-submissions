class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = 0
        hashmap = {}

        for i in range(len(s1)):
            if s1[i] not in hashmap:
                hashmap[s1[i]] = 1
            else:
                hashmap[s1[i]] += 1
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
            else:
                hashmap[s2[i]] = -1

            right += 1
        

        if all(val == 0 for val in hashmap.values()): return True 

        for i in range(right, len(s2)):
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
            else:
                hashmap[s2[i]] = -1
            
            if s2[left] in hashmap:
                hashmap[s2[left]] += 1
            
            left += 1
            
            if all(val == 0 for val in hashmap.values()): return True
        
        return False 


