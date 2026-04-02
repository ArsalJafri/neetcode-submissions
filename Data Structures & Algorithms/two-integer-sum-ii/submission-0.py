class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            d = {}
            
            for i in range(len(numbers)):
                difference = target - numbers[i]
                if difference in d:
                    return [d[difference]+1, i+1]
                else:
                    d[numbers[i]] = i