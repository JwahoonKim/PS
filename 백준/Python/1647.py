from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

path = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    path.append((a, b, cost))

path.sort(key= lambda x: x[2])
parent = list(range(N + 1))


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b


connected_path = []
for a, b, cost in path:
    if find_parent(a) == find_parent(b):
        continue

    union(a, b)
    connected_path.append(cost)

print(sum(connected_path) - max(connected_path))
