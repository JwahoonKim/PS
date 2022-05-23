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
# 이거 n*n을 전부 담으면 안된다. 잘못풀었네
# 힙 이용해서 배열에 상위 5개 값만 계속 담은다음에 마지막에 heap[0] 를 답으로 뺴자