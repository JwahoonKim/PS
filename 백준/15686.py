import sys
from itertools import combinations

INF = int(1e9)
n, m = map(int, input().split())
chicken = []
house = []
city = []
sumArr = []
for i in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
ways = list(combinations(chicken, m))

for way in ways:
    distance = [INF] * len(house)
    for i in way:
        x = i[0]
        y = i[1]
        flag = 0
        for j in range(len(house)):
            dis = abs(x - house[j][0]) + abs(y - house[j][1])
            distance[flag] = min(distance[flag], dis)
            flag += 1
    sumArr.append(sum(distance))
print(min(sumArr))