class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0

        if len(prices) <= 1:
            return profit

        for sell in range(len(prices)):
            if sell + 1 < len(prices):
                if prices[sell + 1] < prices[sell]:
                    profit += prices[sell] - prices[buy]
                    buy = sell + 1

            if sell == len(prices) - 1:
                profit += prices[sell] - prices[buy]

        return profit