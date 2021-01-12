import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
data.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    if i == 0:
        start = data[i][0]
        end = data[i][1]
        count = 1
    else:
        now = data[i]
        start = now[0]
        if start >= end:
            count += 1
            end = now[1]
print(count)
                    