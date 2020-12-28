import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nolisten = []
nosee = []

for i in range(n):
    nolisten.append(input().rstrip())
for i in range(m):
    nosee.append(input().rstrip())

people = list(set(nolisten) & set(nosee))

people.sort()
print(len(people))
for name in people:
    print(name)
