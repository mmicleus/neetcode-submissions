class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        highest = prices[0]
        lowest = prices[0]

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                highest = prices[i]
            
            if prices[i] > highest:

                highest = prices[i]
                profit = highest - lowest

                max_profit = max(max_profit,profit)

        return max_profit