class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, balance):
            if balance < 0:
                return False

            if i == len(s):
                return balance == 0

            if (i, balance) in memo:
                return memo[(i, balance)]

            if s[i] == "(":
                ans = dfs(i + 1, balance + 1)

            elif s[i] == ")":
                ans = dfs(i + 1, balance - 1)

            else:  # "*"
                ans = (
                    dfs(i + 1, balance + 1) or   # treat * as "("
                    dfs(i + 1, balance - 1) or   # treat * as ")"
                    dfs(i + 1, balance)           # treat * as ""
                )

            memo[(i, balance)] = ans
            return ans

        return dfs(0, 0)