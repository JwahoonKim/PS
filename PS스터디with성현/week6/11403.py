n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                if (graph[i][k] + graph[k][j] == 2):
                    graph[i][j] = 1
                    
#join 함수는 리스트의 원소가 str 이여야한다.
for i in graph:
    print(" ".join(map(str, i)))