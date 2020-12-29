# 1. 높이 중 최댓값 찾기
# 2. 비가 0~최댓값 까지 반복
# 4. i 값을 기준으로 dfs
# 마지막 for문 안봐도 되는거 제외할 수 있나?
from sys import *
setrecursionlimit(10 ** 7)

import copy


N = int(input())
graph = []
list1 = []
for i in range(N):
    graph.append(list(map(int,input().split()))) 
G = max(map(max, graph)) # graph에서 최댓값

def dfs(x,y,h,graph):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] > h:
        graph[x][y] = h
        dfs(x - 1, y, h, graph)
        dfs(x + 1, y, h, graph)
        dfs(x, y - 1, h, graph)
        dfs(x, y + 1, h, graph)
        return True
    return False

for h in range(G):
    graph_copy = copy.deepcopy(graph)
    safe = 0
    for i in range(N):
        for j in range(N):
            if dfs(i,j,h,graph_copy) == True:
                safe += 1                
    list1.append(safe)

print(max(list1))
