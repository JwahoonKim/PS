import sys

input = sys.stdin.readline

n, c = map(int, input().split())
answer = 0
houses = []
for _ in range(n):
    x = int(input())
    houses.append(x)

houses.sort()

left = 0
right = int(1e10)

while left <= right:
    # 공유기 간 최소 거리가 mid 라고 가정하자
    mid = (left + right) // 2
    # 첫번째 지점에 이미 설치하고 시작해 --> (c - 1)개 더 설치하면 됨
    iptime = c - 1
    now = 0
    for i in range(1, n):
        distance = houses[i] - houses[now]
        if distance >= mid:
            iptime -= 1
            now = i
        # 공유기를 다 설치 할 수 있는 경우
        if iptime == 0:
            answer = max(answer, mid)
            left = mid + 1
            break
    # 다 설치 못하는 경우
    if iptime > 0:
        right = mid - 1

print(answer)