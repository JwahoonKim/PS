import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
data.sort(key=lambda x: (x[1], x[0]))

# 그리디하게 시간 빨리 끝나는 순서대로 잡으면 됨
for i in range(n):
    # 맨처음
    if i == 0:
        start = data[0][0]
        end = data[0][1]
        count = 1
    else:
        now = data[i]
        start = now[0]
        if start >= end:
            count += 1
            end = now[1]
print(count)
