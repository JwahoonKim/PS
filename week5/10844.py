n = int(input())
arr = [[0] * 10 for _ in range(n + 1)]

for k in range(1, 10):
    arr[1][k] = 1

if n == 1:
    print(9)

else:
    arr[2] = [0,2,2,2,2,2,2,2,2,1]
    
    for i in range(3, n + 1):
        for j in range(1, 10):
            if j == 1:
                arr[i][1] = arr[i - 2][1] + arr[i - 1][2]
            elif j == 9:
                arr[i][9] = arr[i - 1][8]
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j + 1]

    result = sum(arr[n])
    print(result % 1000000000)
