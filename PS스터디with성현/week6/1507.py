#어디 틀린지 모르겠다.
n = int(input())
ans = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#1. 받은 그래프가 유효한 그래프인지 체크
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                ans = -1

#2. i -> j로 가는 간선이 i -> k -> j 로 대체될 수 있다면 i -> j로 가는 간선 삭제
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    graph[i][j] = 0 

#3.2번과정을 수행한 후 그래프는 꼭 필요한 도로만 표시한다. 이를 전부 더한 후 2로 나누면 답             
if ans != -1:
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += graph[i][j] 
    ans = sum // 2

print(ans)