import sys

input = sys.stdin.readline

m = int(input())
a = set()
for i in range(m):
    act = list(input().split())
    if act[0] == "add":
        a.add(int(act[1]))
    elif act[0] == "remove":
        a.discard(int(act[1]))
    elif act[0] == "check":
        print(1) if int(act[1]) in a else print(0)
    elif act[0] == "toggle":
        a.remove(int(act[1])) if int(act[1]) in a else a.add(int(act[1]))
    elif act[0] == "all":
        a = {i for i in range(1, 21)}
    elif act[0] == "empty":
        a = set()
