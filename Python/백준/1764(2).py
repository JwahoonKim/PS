import sys

input = sys.stdin.readline

n, m = map(int, input().split())
no_see = set()
no_listen = set()

# input 받기
for _ in range(n):
    no_see.add(input().rstrip())
for _ in range(m):
    no_listen.add(input().rstrip())

# 교집합
no_listen_see = list(no_see & no_listen)

# 출력부
print(len(no_listen_see))
no_listen_see.sort()
for name in no_listen_see:
    print(name)