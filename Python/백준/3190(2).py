from collections import deque

# 입력받기
n = int(input())

apples = []
k = int(input())
for _ in range(k):
    apples.append(list(map(int, input().split())))

turns = []
L = int(input())
for _ in range(L):
    s, direction = input().split()
    turns.append([int(s), direction])

time = 0
body = deque()
body.append([1, 1])
x, y = 1, 1  # 머리위치
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0

while(1):
    time += 1
    # 몸 늘리기
    nx, ny = x + dx[dir], y + dy[dir]
    # 늘렸는데 벽이면 break
    if not(1 <= nx <= n and 1 <= ny <= n):
        break
    # 늘렸는데 몸이면 break
    if [nx, ny] in body:
        break
    x, y = nx, ny
    body.append([x, y])
    # 사과 있는지 없는지 체크
    if [x, y] not in apples:
        body.popleft()
    else:
        apples.remove([x, y])
    # 방향 전환의 시간인지 체크 + 처리해주기
    if turns:
        t, direction = turns[0]
        if time == t:
            if direction == "D":
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            turns.pop(0)

print(time)
