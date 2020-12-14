# 백준 문제인데 뭐가 틀렸는지 모르겠다..
from collections import deque

N = int(input())
K = int(input())
apple_place = []
for _ in range(K):
    x, y = map(int, input().split())
    apple_place.append((x, y))
L = int(input())
direct = {}
for _ in range(L):
    key, value = input().split()
    direct[int(key)] = value

length = 1
second = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x, y = 1, 1

q = deque()
q.append((x, y))
i = 0
while True:
    x = x + dx[i]
    y = y + dy[i]
    second += 1
    if (x, y) in q or x >= N + 1 or x <= 0 or y >= N + 1 or y <= 0:
        break
    else: 
        q.append((x, y))
    if (x, y) in apple_place:
        length += 1
    if len(q) > length:
        q.popleft()
    if second in direct:
        if direct[second] == "D":
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
print(second)