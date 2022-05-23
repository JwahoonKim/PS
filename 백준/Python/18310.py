n = int(input())
house = list(map(int, input().split()))
house.sort()
# n // 2 - 1 --> 즉 가운데 쪽으로 안테나를 설치해야
# 거리 총 합이 최소가 될 수 있음
print(house[n // 2 - 1])
