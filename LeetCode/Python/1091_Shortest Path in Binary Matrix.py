from collections import deque
from typing import List

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        distance = [[-1] * len(grid[0]) for _ in range(len(grid))]
        q = deque()
        q.append((0, 0, 1))

        while q:
            r, c, dist = q.popleft()

            if distance[r][c] == -1 or distance[r][c] > dist:
                distance[r][c] = dist

                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 0 and distance[nr][nc] == -1 or distance[nr][nc] > dist + 1:
                            q.append((nr, nc, dist + 1))

        return distance[-1][-1]


print(Solution().shortestPathBinaryMatrix([[0,1],[1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
