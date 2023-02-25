from typing import List


def can_fall(r, c, grid):
    if r == len(grid):
        return c
    if c == 0 and grid[r][c] == -1:
        return -1
    if c == len(grid[0]) - 1 and grid[r][c] == 1:
        return -1
    if grid[r][c] == 1:
        if grid[r][c] != grid[r][c + 1]:
            return -1
        return can_fall(r + 1, c + 1, grid)
    else:
        if grid[r][c] != grid[r][c - 1]:
            return -1
        return can_fall(r + 1, c - 1, grid)


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = [-1] * len(grid[0])
        for i in range(len(grid[0])):
            answer[i] = can_fall(0, i, grid)
        return answer

print(Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))