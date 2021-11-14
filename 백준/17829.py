n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

while(n > 1):
    next_matrix = []
    line = []
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            # 두번째로 큰수
            second_num = sorted([matrix[i][j], matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]])[2]
            line.append(second_num)
            if len(line) == n // 2:
                next_matrix.append(line)
                line = []
    matrix = next_matrix
    n //= 2

print(matrix[0][0])