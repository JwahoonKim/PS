from collections import deque
from typing import List


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def insert_rotten_orange(q, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i, j, 0))


def not_all_rotten(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return True
    return False


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        insert_rotten_orange(q, grid)

        while q:
            r, c, day = q.popleft()

            if visited[r][c]:
                continue

            answer = day
            visited[r][c] = True
            grid[r][c] = 2

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    q.append([nr, nc, day + 1])

        if not_all_rotten(grid):
            return -1

        return answer
