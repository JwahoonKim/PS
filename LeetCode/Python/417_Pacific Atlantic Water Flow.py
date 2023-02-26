from typing import List

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(heights, r, c, visited):
    visited[r][c] = True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and not visited[nr][nc] and heights[r][c] <= heights[nr][nc]:
            dfs(heights, nr, nc, visited)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer = []
        m, n = len(heights), len(heights[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        for i in range(m):
            dfs(heights, i, 0, p_visited)
            dfs(heights, i, n - 1, a_visited)

        for i in range(n):
            dfs(heights, 0, i, p_visited)
            dfs(heights, m - 1, i, a_visited)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    answer.append([i, j])

        return answer


Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])