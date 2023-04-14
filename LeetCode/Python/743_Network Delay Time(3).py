import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k -> 최대 걸린 시간 노드 찾기
        # 다익스트라 시작
        graph = defaultdict(list)
        INF = int(1e9)
        distance = [0] + [INF] * n

        for time in times:
            start, end, dist = time
            graph[start].append([end, dist])

        priority_q = [(0, k)]
        while priority_q:
            dist, node = heapq.heappop(priority_q)
            if distance[node] != INF:
                continue

            distance[node] = dist
            next_nodes_and_dists = graph[node]

            for next_node, next_dist in next_nodes_and_dists:
                heapq.heappush(priority_q, (distance[node] + next_dist, next_node))

        if INF in distance:
            return -1

        return max(distance)


Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)