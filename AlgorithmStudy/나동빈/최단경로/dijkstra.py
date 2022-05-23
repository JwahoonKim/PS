# O(n^2) 시간복잡도가 소요됨
import sys
input = sys.stdin.readline
INF = 987654321

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
# 경로정보를 graph에 담기 a -> b로 가는 경로는 c만큼 소요
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallests_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for j in range(n - 1):
        now = get_smallests_node()
        visited[now] = True
        for k in graph[now]:
            cost = distance[now] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost

dijkstra(start)

print(distance)

