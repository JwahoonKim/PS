import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(V + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
for a, b, cost in edges:
    if find_parent(a) == find_parent(b):
        continue
    union(a, b)
    answer += cost

print(answer)
