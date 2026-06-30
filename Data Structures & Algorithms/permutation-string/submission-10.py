class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = 0
        hashmap = {}

        # 1. Build the Target Board entirely first
        for i in range(len(s1)):
            if s1[i] not in hashmap:
                hashmap[s1[i]] = 1
            else:
                hashmap[s1[i]] += 1
                
        # 2. Now that the board is built, process the first window
        for i in range(len(s1)):
            # ONLY care about it if it's a target letter!
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
            
            right += 1
        
        # Check if the very first window was a hole-in-one
        if all(val == 0 for val in hashmap.values()): 
            return True 

        # 3. Engine Phase: Slide the box to the right
        for i in range(right, len(s2)):
            # ONLY care about the new letter if it's a target letter!
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
            
            # ONLY care about the old letter if it's a target letter!
            if s2[left] in hashmap:
                hashmap[s2[left]] += 1
            
            left += 1
            
            # Check the board after the step
            if all(val == 0 for val in hashmap.values()): 
                return True
        
        return False


