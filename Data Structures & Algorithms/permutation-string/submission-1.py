class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        left = 0
        arr2 = [0] * 26
        arr1 = [0] * 26
        matches = 0
       

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

                    
        for i in range(26):
            matches += (1 if arr1[i] == arr2[i] else 0)

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True 
            
            index1 = ord(s2[right])  - ord('a') 

            arr2[index1] +=1 

            if arr1[index1] == arr2[index1]:
                matches += 1
            elif arr1[index1] + 1 == arr2[index1]:
                matches -= 1
            
            index2 = ord(s2[left]) - ord('a') 

            arr2[index2] -= 1
            if arr1[index2] == arr2[index2]:
                matches += 1
            elif arr1[index2] - 1 == arr2[index2]:
                matches -= 1 
            
            left += 1

        return matches == 26
                


            