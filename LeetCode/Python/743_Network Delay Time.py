from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))
        
        INF = int(1e9)
        distance = [INF] * (n + 1)
        visited = [False] * (n + 1)
        
        q = [(0, k)]
        
        while q:
            time, now = heappop(q)
            
            if visited[now]:
                continue
                
            visited[now] = True
            distance[now] = time
            
            for end, next_time in graph[now]:
                if not visited[end]:
                    heappush(q, (next_time + time, end))
        
        if INF not in distance[1:]:
            return max(distance[1:])
        return -1