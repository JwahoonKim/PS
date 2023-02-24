from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [int(1e9)] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            a1 = dp[i - 2] + cost[i]
            a2 = dp[i - 1] + cost[i]
            dp[i] = min(a1, a2)

        return min(dp[-2], dp[-1])
