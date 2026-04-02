class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}
        for numbers in nums:
            if numbers not in dictionary:
                dictionary[numbers] = 1
            elif numbers in dictionary:
                dictionary[numbers] += 1 
        
        tupleList = [(key, value) for key, value in dictionary.items()]
        buckets = [ [] for freq in range(len(nums) +1)]

        for numbers, freq in tupleList:
            buckets[freq].append(numbers)
        finalList = []
        counter = 0
        for i in range(len(buckets)-1, 0, -1):
            for nums in buckets[i]:
                finalList.append(nums)
                counter +=1
                if counter == k:
                    return finalList

