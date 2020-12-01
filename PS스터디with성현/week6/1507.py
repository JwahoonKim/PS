#어디 틀린지 모르겠다.

n = int(input())
ans = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                ans = -1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    graph[i][j] = 0 
                
if ans != -1:
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += graph[i][j] 
    ans = sum // 2

print(ans)