from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(len(dp)):
            if dp[i] == INF:
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == INF else dp[amount]

Solution().coinChange(coins = [1,2,5], amount = 11)