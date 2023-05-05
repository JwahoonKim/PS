from typing import List

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(grid, r, c, visited):
    answer = 1

    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return 0

    if visited[r][c] or grid[r][c] == 0:
        return 0

    visited[r][c] = True

    for i in range(4):
        answer += dfs(grid, r + dr[i], c + dc[i], visited)

    return answer


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        answer = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    answer = max(answer, dfs(grid, i, j, visited))

        return answer

Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
