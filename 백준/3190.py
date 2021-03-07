from collections import deque

# 입력받기
n = int(input())
k = int(input())
apple = []
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))
m = int(input())
turn = []
for _ in range(m):
    time, dir = input().split()
    time, dir = int(time), str(dir)
    turn.append((time, dir))
turn.sort(reverse=True)

answer = 0
body = deque()
body.append((1, 1))
# 머리위치(x, y)
x, y = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

# 게임 시작
while 1:
    answer += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 벽에 닿았으면 종료
    if 1 > nx or nx > n or 1 > ny or ny > n:
        break
    # 자기 몸에 닿을 경우 종료
    if (nx, ny) in body:
        break
    # 그렇지 않은 경우 몸 옮기기
    body.append((nx, ny))
    x, y = nx, ny
    # 사과가 있으면 몸길이 유지
    if (x, y) in apple:
        apple.remove((x, y))
    # 사과가 없으면 몸길이 줄이기
    else:
        body.popleft()
    # 방향 전환의 시간인지 체크하기
    if len(turn) >= 1:
        if answer == turn[-1][0]:
            if turn[-1][1] == "D":
                dir = (dir + 1) % 4
            if turn[-1][1] == "L":
                dir = (dir - 1) % 4
            turn.pop()

print(answer)