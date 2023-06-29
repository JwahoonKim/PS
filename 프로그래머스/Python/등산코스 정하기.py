import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    graph = defaultdict(list)

    # 그래프 만들기
    for start, end, time in paths:
        graph[start].append((end, time))
        graph[end].append((start, time))

    summits_set = set(summits)

    q = []
    visited = [False] * (n + 1)

    # 시작점들과 연결된 간선들을 큐에 넣기
    for gate in gates:
        adjs = graph[gate]
        for next_node, time in adjs:
            heapq.heappush(q, (time, next_node))

    # 답이 여러 개일 수 있어 answer_summits에 넣어두고
    # 추후 정렬하여 산봉우리가 가작 작은 것을 찾기
    answer_summits = []

    while q:
        time, node = heapq.heappop(q)

        # 산봉우리 발견
        if node in summits_set:
            answer_summits.append([node, time])
            continue

        # 이미 방문한 곳이면 넘어가기 -> 2번째 말한 포인트를 사용한 부분
        if visited[node]:
            continue
        visited[node] = True

        adjs = graph[node]
        for next_node, next_time in adjs:
            if not visited[next_node]:
                heapq.heappush(q, (max(time, next_time), next_node))

    # 가장 작은 산봉우리 번호를 찾기 위해 정렬
    answer_summits.sort(key=lambda x: (x[1], x[0]))
    return answer_summits[0]

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
