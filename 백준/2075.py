N = int(input())
graph = []
for i in range(N):
    data = sorted(list(map(int, input().split())))
    graph.append(data)

for i in range(N):
    largest = []
    for j in range(N):
        largest.append(graph[j][-1])
    largestIndex = largest.index(max(largest))
    answer = graph[largestIndex].pop(-1)

print(answer)
