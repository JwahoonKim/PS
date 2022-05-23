from collections import deque

#변수 설정 및 입력값 받기
N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

#간선의 개수만큼 그래프에 표기
for i in range(M):
    n,m = map(int,input().split())
    graph[n].append(m)
    graph[m].append(n)

#작은수 순서대로 정렬    
for i in range(N):
    graph[i].sort()
#for x in graph:
#   x.sort() 로 해도 됨

#dfs
def dfs(graph,start,visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph,i,visited)

#bfs
def bfs(graph,start,visited):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        v = que.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                que.append(i)

#dfs,bfs함수 실행
dfs(graph,V,visited1)
print("")
bfs(graph,V,visited2)
