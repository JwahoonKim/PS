import sys

input = sys.stdin.readline

n = int(input())

x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

xr, yr = 0, 0
for i in range(n):
    xr += x[i] * y[i + 1]
    yr += y[i] * x[i + 1]

print(round(abs((xr - yr) / 2), 1))