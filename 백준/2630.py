import sys
input = sys.stdin.readline

def checkblue(graph):
    a = len(graph)
    for i in range(a):
        for j in range(a):
            if graph[i][j] == 0:
                return False
    return True

def checkwhite(graph):
    a = len(graph)
    for i in range(a):
        for j in range(a):
            if graph[i][j] == 1:
                return False
    return True

n = int(input())
white = 0
blue = 0
colors = []
for i in range(n):
    colors.append(list(map(int, input().split())))

