n, k = map(int, input().split())
graph = []
for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        graph.append((w, v))

