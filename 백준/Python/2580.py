# 스도쿠가 유효한지 체크하는 함수
def isValid(arr):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 가로줄 체크
    for i in range(9):
        for j in range(9):
            if sorted(arr[i]) == numbers:
                continue
            else:
                return False
    # 세로줄 체크
    for i in range(9):
        col = []
        for j in range(9):
            col.append(arr[j][i])
        if sorted(col) == numbers:
            continue
        else:
            return False
    # 3 X 3 체크
    for k in range(0, 6, 3):
        for m in range(0, 6, 3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(arr[i + k][j + m])
            if sorted(square) == numbers:
                continue
            else:
                return False
    return True
