class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        hashmap = {}

        for char_s, char_t in zip(s,t):
            hashmap[char_s] = hashmap.get(char_s, 0) + 1
            hashmap[char_t] = hashmap.get(char_t, 0) - 1
        
        return all(values == 0 for values in hashmap.values()) 