# 2*2인 곳을 찾아서 그 위치를 0으로 만들고 터진 블록 개수 세는 함수
def pop(m, n, board):
    answer = 0
    # 문자열로된 board를 char로 list만듬 --> 0 집어넣으려고
    splitBoard = []
    for i in board:
        splitBoard.append(list(i))
    TwobyTwoLocation = []
    for i in range(m - 1):
        for j in range(n - 1):
            count = 0
            # splitBoard[i][j] != 0인 조건 추가해야함
            if splitBoard[i][j] != 0:
                if (
                    splitBoard[i][j] == splitBoard[i + 1][j]
                    and splitBoard[i + 1][j] == splitBoard[i + 1][j + 1]
                    and splitBoard[i + 1][j + 1] == splitBoard[i][j + 1]
                ):
                    TwobyTwoLocation.append((i, j))
    for location in TwobyTwoLocation:
        x, y = location[0], location[1]
        for i in range(2):
            for j in range(2):
                if splitBoard[x + i][y + j] != 0:
                    splitBoard[x + i][y + j] = 0
                    answer += 1
    return splitBoard, answer


# pop을 하고난 뒤 drop하는 함수
def drop(board):
    for _ in range(len(board)):
        for i in range(1, len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and board[i - 1][j] != 0:
                    board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
    return board


def solution(m, n, board):
    total = 0
    while 1:
        newBoard, answer = pop(m, n, board)
        if newBoard == board:
            return total
        total += answer
        board = drop(newBoard)


if __name__ == "__main__":
    board = ["TTT", "TTT", "TTT"]
    m, n = 3, 3
    print(solution(m, n, board))
