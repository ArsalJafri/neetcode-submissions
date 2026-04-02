class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0

        for i in range(len(prices)):
            if prices[left] < prices[i]:
                profit = max(profit, prices[i] - prices[left])
            else:
                left = i
                
        return profit