from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)

while 1:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break

    graph[a].append(b)
    graph[b].append(a)

distances = [51] * (n + 1)


def bfs(i):
    global n
    result = 0
    visited = [False] * (n + 1)
    q = deque()
    q.append((i, 0))
    while q:
        now, dist = q.popleft()
        if visited[now]:
            continue
        visited[now] = True

        if dist > result:
            result = dist

        for _next in graph[now]:
            if not visited[_next]:
                q.append((_next, dist + 1))

    return result


for i in range(1, n + 1):
    distances[i] = bfs(i)

minScore = min(distances)
candidateCnt = 0
candidates = []

for n, score in enumerate(distances):
    if score == minScore:
        candidateCnt += 1
        candidates.append(n)

print(minScore, candidateCnt)
print(' '.join(map(str, candidates)))
