def rotate(arr):
    n = len(arr)
    m = len(arr[0])
    afterRotate = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            afterRotate[j][n - i - 1] = arr[i][j]
    return afterRotate

def mirror(arr):
    n = len(arr)
    m = len(arr[0])
    afterMirror = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            afterMirror[i][m - j - 1] = arr[i][j]
    return afterMirror

arr= [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
mir = mirror(arr)
print(mir)