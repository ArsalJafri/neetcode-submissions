class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = 0

        while left <= right:
            mid = (right + left) // 2
            countHours = 0

            for pile in piles:
                countHours += math.ceil(pile/mid)
            
            if countHours <= h:
                right = mid - 1
                speed = mid
            else:
                left = mid + 1
        
        return speed