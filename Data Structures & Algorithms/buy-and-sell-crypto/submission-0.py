class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minimumPrice = prices[0]

        for i in prices:
            if i < minimumPrice:
                minimumPrice = i
            answer = max(answer, i - minimumPrice)

        return answer
           