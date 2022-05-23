import heapq

A, B, N = map(int, input().split())
now = 1
number = 1
blue = []
red = []
q = []

for i in range(N):
    start, color, count = input().split()
    start = int(start)
    count = int(count)
    for j in range(count):
        if color == "B":
            heapq.heappush(q, (start, "blue"))
            start += A
        else:
            heapq.heappush(q, (start, "red"))
            start += B
for i in range(len(q)):
    time, color = heapq.heappop(q)
    if color == "blue":
        blue.append(number)
        number += 1
    else:
        red.append(number)
        number += 1

print(len(blue))
print(" ".join(map(str, blue)))
print(len(red))
print(" ".join(map(str, red)))
