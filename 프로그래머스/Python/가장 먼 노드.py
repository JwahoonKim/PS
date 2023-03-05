import heapq
from collections import defaultdict


def solution(n, vertex):
    graph = defaultdict(list)
    for start, end in vertex:
        graph[start].append(end)
        graph[end].append(start)

    INF = int(1e9)
    distances = [-1] * (n + 1)
    visited = [False] * (n + 1)
    q = [(0, 1)]
    while q:
        dist, node = heapq.heappop(q)

        if visited[node]:
            continue

        visited[node] = True
        distances[node] = dist

        for next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(q, (dist + 1, next_node))

    max_distance = max(distances)
    return get_answer(distances, max_distance)


def get_answer(distances, max_distance):
    answer = 0
    for dist in distances:
        if dist == max_distance:
            answer += 1
    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])