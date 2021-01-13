import sys

input = sys.stdin.readline


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


def straight(arr):
    n = len(arr)
    m = len(arr[0])
    ans = 0
    value = 0
    for i in range(n - 3):
        for j in range(m):
            value += arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
            ans = max(value, ans)
            value = 0
    return ans


def box(arr):
    n = len(arr)
    m = len(arr[0])
    ans = 0
    value = 0
    for i in range(n - 1):
        for j in range(m - 1):
            value = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            ans = max(ans, value)
            value = 0
    return ans


def nieun(arr):
    n = len(arr)
    m = len(arr[0])
    ans = 0
    value = 0
    for i in range(n - 2):
        for j in range(m - 1):
            value = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
            ans = max(ans, value)
            value = 0
    return ans


def rieul(arr):
    n = len(arr)
    m = len(arr[0])
    ans = 0
    value = 0
    for i in range(n - 2):
        for j in range(m - 1):
            value = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            ans = max(ans, value)
            value = 0
    return ans


def centerFinger(arr):
    n = len(arr)
    m = len(arr[0])
    ans = 0
    value = 0
    for i in range(n - 1):
        for j in range(m - 2):
            value = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
            ans = max(ans, value)
            value = 0
    return ans


def findMax(arr):
    way1 = straight(arr)
    way2 = box(arr)
    way3 = rieul(arr)
    way4 = nieun(arr)
    way5 = centerFinger(arr)
    answer = max(way1, way2, way3, way4, way5)
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = []
    for i in range(n):
        numbers.append(list(map(int, input().split())))
    answer = 0
    # 그대로 최댓값 찾기
    answer = findMax(numbers)
    # 시계방향 90도 회전해서 해보기
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 180도
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 270도
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 다시 원상태로 만든 뒤 대칭만들고 최댓값 찾기
    numbers = rotate(numbers)
    numbers = mirror(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 90도
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 180도
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 270도
    numbers = rotate(numbers)
    result = findMax(numbers)
    answer = max(answer, result)
    # 답 내기
    print(answer)