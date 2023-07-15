sudoku = [[] for _ in range(9)]
numbers = list(range(1, 10))

for i in range(9):
    sudoku[i] = list(map(int, input()))

answers = []


def flat(arr):
    result = ""
    for line in arr:
        result += ''.join(map(str, line))
    return result


def row_check(row, col, number):
    for i in range(9):
        if sudoku[row][i] == number:
            return False
    return True


def col_check(row, col, number):
    for i in range(9):
        if sudoku[i][col] == number:
            return False
    return True


def square_check(row, col, number):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == number:
                return False
    return True


def can_put(row, col, number):
    if row_check(row, col, number) and col_check(row, col, number) and square_check(row, col, number):
        return True
    return False


def go(place):
    if answers:
        return

    row = place // 9
    col = place % 9
    if place == 81:
        answers.append(flat(sudoku))
        return

    if sudoku[row][col] != 0:
        go(place + 1)
        return

    for number in numbers:
        if can_put(row, col, number):
            sudoku[row][col] = number
            go(place + 1)
            sudoku[row][col] = 0


go(0)
answers.sort()
answer = answers[0]

for i in range(9):
    print(answer[9 * i: 9 * i + 9])
