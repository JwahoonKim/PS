import sys
from sys import *
setrecursionlimit(10 ** 7) 

m,n,k = map(int,input().split())
graph = [[1]*n for _ in range(m)]
count = 0
house = 0
arr = []
def dfs(x,y,graph):
    if (0 <= x < m and 0 <= y < n):
        if graph[x][y] == 1:
            graph[x][y] = 0
            global house
            house += 1
            dfs(x - 1, y,graph)
            dfs(x, y - 1,graph)
            dfs(x + 1, y,graph)
            dfs(x, y + 1,graph)
            return True
    return False

for i in range(k):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    for j in range(y1,y2):
        for l in range(x1, x2):
            graph[j][l] = 0

for i in range(m):
    for j in range(n):
        if dfs(i,j,graph) == True:
            count += 1
            arr.append(house)
        house = 0
    
print(count)
arr.sort()
for i in range(len(arr)):
    print(arr[i], end= " ")