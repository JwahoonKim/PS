import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node, edge = map(int, input().split())
count = 0
graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if visited[x] == False:
        visited[x] = True
        for i in graph[x]:
            dfs(i)
        return True
    return False

for i in range(1, len(graph)):
    if dfs(i) == True:
        count += 1
    
print(count)