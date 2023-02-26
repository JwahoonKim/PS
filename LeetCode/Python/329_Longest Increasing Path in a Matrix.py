from typing import List

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, matrix, memo):
    if memo[r][c] != 0:
        return memo[r][c]

    res = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(memo) and 0 <= nc < len(memo[0]):
            if matrix[nr][nc] > matrix[r][c]:
                dist = dfs(nr, nc, matrix, memo)
                if dist > res:
                    res = dist
    memo[r][c] = res + 1
    return memo[r][c]


def get_max(memo):
    result = 1
    for i in range(len(memo)):
        for j in range(len(memo[0])):
            if memo[i][j] > result:
                result = memo[i][j]
    return result


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, matrix, memo)

        return get_max(memo)


Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])