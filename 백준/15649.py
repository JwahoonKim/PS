from itertools import permutations

n, m = map(int, input().split())
arr = list(permutations(range(1, n + 1), m))

for i in arr:
    for j in range(m):
        print(i[j], end = ' ')
    print('')
