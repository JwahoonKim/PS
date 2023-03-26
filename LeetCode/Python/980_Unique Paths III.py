from typing import List


class Solution:
    answer = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    start = (0, 0)
    end = (0, 0)

    def dfs(self, r, c, visited, grid, cnt):
        if 0 <= r < len(visited) and 0 <= c < len(visited[0]):
            if (r, c) == (self.end[0], self.end[1]) and cnt == 0:
                self.answer += 1
                return

            for i in range(4):
                nr = r + self.dr[i]
                nc = c + self.dc[i]
                if 0 <= nr < len(visited) and 0 <= nc < len(visited[0]):
                    if not visited[nr][nc] and grid[nr][nc] != -1:
                        visited[nr][nc] = True
                        self.dfs(nr, nc, visited, grid, cnt - 1)
                        visited[nr][nc] = False

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        cnt = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    cnt += 1
                elif grid[i][j] == 1:
                    self.start = (i, j)
                elif grid[i][j] == 2:
                    self.end = (i, j)

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        visited[self.start[0]][self.start[1]] = True
        self.dfs(self.start[0], self.start[1], visited, grid, cnt)
        return self.answer
