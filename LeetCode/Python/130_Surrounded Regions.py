from typing import List

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(board, r, c, visited):
    if not (0 <= r < len(board) and 0 <= c < len(board[0])):
        return

    if visited[r][c]:
        return

    if board[r][c] == "O":
        visited[r][c] = True
        for i in range(4):
            dfs(board, r + dr[i], c + dc[i], visited)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board[0])):
            if board[0][i] == "O" and not visited[0][i]:
                dfs(board, 0, i, visited)

        for i in range(len(board[0])):
            if board[len(board) - 1][i] == "O" and not visited[len(board) - 1][i]:
                dfs(board, len(board) - 1, i, visited)

        for i in range(len(board)):
            if board[i][0] == "O" and not visited[i][0]:
                dfs(board, i, 0, visited)

        for i in range(len(board)):
            if board[i][len(board[0]) - 1] == "O" and not visited[i][len(board[0]) - 1]:
                dfs(board, i, len(board[0]) - 1, visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

