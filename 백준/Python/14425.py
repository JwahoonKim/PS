import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 왜 dict는 원소찾기 시간복잡도가 1임?
s = dict()
answer = 0

for i in range(n):
    s[input().rstrip()] = 1

for _ in range(m):
    a = input().rstrip()
    if a in s:
        answer += 1
print(answer)