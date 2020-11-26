from collections import deque
#여러 변수 , 입력값 설정
N = int(input()) 
E = int(input())
graph = [[] for _ in range(N+1)] 
visited = [False]*(N+1) 

for i in range(E):
    n,m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

#dfs함수 만들기
def bfs(graph, start, visited):
    que = deque([start])
    count = 0
    visited[start] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True
                count += 1
    return count

print(bfs(graph,1,visited))

