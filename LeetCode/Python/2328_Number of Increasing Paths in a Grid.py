from typing import List

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
mod = 10 ** 9 + 7


def dfs(r, c, grid, dp):
    if dp[r][c] != 0:
        return dp[r][c]

    result = 1
    now_value = grid[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            next_value = grid[nr][nc]
            if now_value < next_value:
                result += dfs(nr, nc, grid, dp) % mod
    dp[r][c] = result % mod
    return result


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0:
                    dfs(i, j, grid, dp)

        return sum(map(sum, dp)) % mod
