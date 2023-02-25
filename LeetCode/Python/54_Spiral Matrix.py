from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r_len = len(matrix)
        c_len = len(matrix[0])
        dc = [1, 0, -1, 0]
        dr = [0, 1, 0, -1]
        visited = [[False] * c_len for _ in range(r_len)]
        r, c, dir = 0, 0, 0

        answer = []
        for _ in range(r_len * c_len):
            answer.append(matrix[r][c])
            visited[r][c] = True
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < r_len and 0 <= nc < c_len and not visited[nr][nc]:
                r, c = nr, nc
            else:
                dir = (dir + 1) % 4
                r += dr[dir]
                c += dc[dir]
        return answer

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
