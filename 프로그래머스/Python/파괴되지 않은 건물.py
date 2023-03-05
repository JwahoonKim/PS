def col_sum(acc_sum):
    for c in range(len(acc_sum[0])):
        for r in range(len(acc_sum)):
            if r == 0:
                continue
            acc_sum[r][c] += acc_sum[r - 1][c]


def row_sum(acc_sum):
    for r in range(len(acc_sum)):
        for c in range(len(acc_sum[0])):
            if c == 0:
                continue
            acc_sum[r][c] += acc_sum[r][c - 1]


def apply_acc_sum_to_board(acc_sum, board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += acc_sum[r][c]


def get_answer(board):
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] >= 1:
                answer += 1
    return answer


def solution(board, skill):
    n = len(board)
    m = len(board[0])
    acc_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree

        acc_sum[r1][c1] += degree
        acc_sum[r1][c2 + 1] -= degree
        acc_sum[r2 + 1][c1] -= degree
        acc_sum[r2 + 1][c2 + 1] += degree

    col_sum(acc_sum)
    row_sum(acc_sum)
    apply_acc_sum_to_board(acc_sum, board)

    return get_answer(board)
    

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], 	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))


