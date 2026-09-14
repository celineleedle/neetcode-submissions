class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentMin = prices[0]

        for price in prices:
            if price < currentMin:
                currentMin = price
            else:
                profit = price - currentMin

                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit