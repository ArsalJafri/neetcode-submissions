class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_number = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_number
            max_number = max(max_number, temp)        
            
        return arr