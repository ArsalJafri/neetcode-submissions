class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        smallestSpeed = 0
    
        while left <= right:
            mid = (right + left) // 2
            countHours = 0

            for pile in piles:
                countHours += math.ceil(pile / mid)

            if countHours <= h:
                smallestSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return smallestSpeed
                
                    
