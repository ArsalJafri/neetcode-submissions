class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(len(prices)):
            #first check if right is less then left, if so new left
            if prices[right] < prices[left]:
                left = right
            
            profit = max(profit, prices[right] - prices[left])

        return profit