from copy import deepcopy
from typing import List


def col_check(r, c, board):
    for i in range(r - 1, -1, -1):
        if board[i][c] == 'Q':
            return False
    return True


def diagonal_check(r, c, board):
    for i in range(1, r + 1):
        if c - i >= 0 and board[r - i][c - i] == 'Q':
            return False
        if c + i < len(board) and board[r - i][c + i] == 'Q':
            return False
    return True


def can_put(r, c, board, n):
    if r == 0:
        return True

    if col_check(r, c, board) and diagonal_check(r, c, board):
        return True

    return False


def go(r, board, answer, n):
    if r == n:
        answer.append(deepcopy(board))
        return

    for i in range(n):
        if can_put(r, i, board, n):
            board[r] = '.' * i + 'Q' + '.' * (n - i - 1)
            go(r + 1, board, answer, n)
            board[r] = '.' * n


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        board = ["." * n for _ in range(n)]
        go(0, board, answer, n)
        return answer


Solution().solveNQueens(4)