h, w = map(int, input().split())
wall = list(map(int, input().split()))
count = 0
# (좌 최대) 기준 (우 최대)  --> min(좌 최대, 우 최대) - 기준 == 기준에서 빗물 총량
for i in range(1, w - 1):
    nowHeight = wall[i]
    leftMax = max(wall[:i])
    rightMax = max(wall[i + 1 :])
    water = min(leftMax, rightMax) - nowHeight
    # water 가 양수값인 경우만 의미가 있음
    if water <= 0:
        continue
    count += water
print(count)