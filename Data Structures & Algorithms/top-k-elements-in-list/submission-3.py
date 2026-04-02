class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        #bucket sort... 
        array = [[] for _ in range(len(nums) + 1)] 

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        for num, freq in hashmap.items():
           array[freq].append(num)
        

        result = []
        for i in range(len(array) - 1, -1, -1):
            for num in array[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
