from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        answer = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    line_cnt = 4
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == 1:
                            line_cnt -= 1
                    answer += line_cnt

        return answer

