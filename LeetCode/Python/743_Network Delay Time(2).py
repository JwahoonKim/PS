import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        graph = defaultdict(list)
        distance = [INF] * (n + 1)

        for u, v, w in times:
            graph[u].append((w, v))

        q = [(0, k)]
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] == INF:
                distance[now] = dist
            for d, nextNode in graph[now]:
                if dist + d < distance[nextNode]:
                    heapq.heappush(q, (dist + d, nextNode))

        return max(distance[1:]) if INF not in distance[1:] else -1

print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], n = 3, k = 1))