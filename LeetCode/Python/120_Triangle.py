from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INF = int(1e9)
        dp = [[INF] * len(triangle[i]) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for h in range(len(triangle) - 1):
            for c in range(len(triangle[h])):
                dp[h + 1][c] = min(dp[h + 1][c], dp[h][c] + triangle[h + 1][c])
                dp[h + 1][c + 1] = min(dp[h + 1][c + 1], dp[h][c] + triangle[h + 1][c + 1])

        return min(dp[-1])
