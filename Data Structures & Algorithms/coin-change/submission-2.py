class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            res = float("inf")

            for c in coins:
                var1 = dfs(amount - c) + 1
                
                res = min(res, var1)
            
            memo[amount] = res

            return res
        
        var2 = dfs(amount)

        if var2 == float("inf"):
            return -1

        return var2