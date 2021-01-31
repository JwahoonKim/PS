from math import floor

# floor ( y / x * 100)은 왜 틀리지?

x, y = map(int, input().split())
winrate = floor(100 * y / x)
answer = 0
left, right = 0, 1000000000
# 승률이 바뀌지 않는 경우
if winrate >= 99:
    answer = -1
else:
    while left <= right:
        mid = (left + right) // 2
        nx, ny = x + mid, y + mid
        if floor(100 * ny / nx) > winrate:
            right = mid - 1
        else:
            left = mid + 1
    answer = right + 1
print(answer)
