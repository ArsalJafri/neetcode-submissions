class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        
        hashmap = {}
        
        # 1. Build the Target Board
        for char in s1:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
                
        # The "Perfect Score" is exactly the number of unique letters in s1
        target_score = len(hashmap)
        
        # 2. Setup Phase: Process the very first window of s2
        for i in range(len(s1)):
            if s2[i] in hashmap:
                hashmap[s2[i]] -= 1
        
        # 3. Calculate initial matches for the starting window
        matches = 0
        for val in hashmap.values():
            if val == 0:
                matches += 1
                
        if matches == target_score:
            return True 

        # 4. Engine Phase
        left = 0
        for right in range(len(s1), len(s2)):
            new_char = s2[right]
            old_char = s2[left]
            
            # --- PROCESS NEW INCOMING LETTER ---
            if new_char in hashmap:
                # If it's currently 1, subtracting 1 will make it 0 (Perfect!)
                if hashmap[new_char] == 1:
                    matches += 1
                # If it's currently 0, subtracting 1 will make it -1 (Broken!)
                elif hashmap[new_char] == 0:
                    matches -= 1
                
                hashmap[new_char] -= 1
            
            # --- PROCESS OLD OUTGOING LETTER ---
            if old_char in hashmap:
                # If it's currently -1, adding 1 will make it 0 (Perfect!)
                if hashmap[old_char] == -1:
                    matches += 1
                # If it's currently 0, adding 1 will make it 1 (Broken!)
                elif hashmap[old_char] == 0:
                    matches -= 1
                
                hashmap[old_char] += 1
            
            left += 1
            
            # Instant check: No loops, no scanning!
            if matches == target_score:
                return True
        
        return False


