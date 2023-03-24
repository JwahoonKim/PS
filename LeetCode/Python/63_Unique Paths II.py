from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0] * c for i in range(r)]

        for i in range(c):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1

        for i in range(r):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])