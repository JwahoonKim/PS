import sys

input = sys.stdin.readline

n = int(input())
lectures = []
money = 0
time = 1
for i in range(n):
    pay, day = map(int, input().split())
    lectures.append([pay, day])

lectures = sorted(lectures, key = lambda x : x[0], reverse=True)

for i in range(len(lectures)):
    pay, day = lectures[i]
    if day > 0:
        money += pay
        for j in range(i, len(lectures)):
            lectures[j][1] -= 1
    else:
        continue
print(money)