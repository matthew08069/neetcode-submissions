class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for l in range(len(prices) - 1):
            r = l + 1
            while r < len(prices):
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1

        return max_profit
