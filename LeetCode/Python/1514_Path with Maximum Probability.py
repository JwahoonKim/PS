from collections import deque, defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        prob_memo = [0] * n
        graph = defaultdict(list)
        for (x, y), p in zip(edges, succProb):
            graph[x].append((y, p))
            graph[y].append((x, p))

        q = deque()
        q.append((start, 1))
        while q:
            node, prob = q.popleft()
            if prob_memo[node] > prob:
                continue
            prob_memo[node] = prob

            for next_node, p in graph[node]:
                next_prob = prob * p
                if prob_memo[next_node] < next_prob:
                    q.append((next_node, next_prob))

        return prob_memo[end]


print(Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))