from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        answer = 0
        graph = defaultdict(list)

        for i, manager in enumerate(manager):
            if manager != -1:
                graph[manager].append(i)

        q = deque()
        q.append((headID, 0))

        while q:
            id, time = q.popleft()

            if time > answer:
                answer = time

            adjs = graph[id]
            for adj in adjs:
                q.append((adj, time + informTime[id]))

        return answer
    