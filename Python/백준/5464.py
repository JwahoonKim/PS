from collections import deque

n, m = map(int, input().split())
park_cost = []
park_car_info = [0] * n
cars = [0]
wait_cars = deque()
total_cost = 0

for _ in range(n):
    park_cost.append(int(input()))
for _ in range(m):
    cars.append(int(input()))

for _ in range(2 * m):
    car = int(input())
    if car > 0:
        # 주차장이 하나라도 비어있으면
        if 0 in park_car_info:
            for i in range(n):
                if park_car_info[i] == 0:
                    park_car_info[i] = car
                    total_cost += cars[car] * park_cost[i]
                    break
        else:
            wait_cars.append(car)
    # 차가 나갈때
    elif car < 0:
        car = -car
        parking_space = park_car_info.index(car)
        park_car_info[parking_space] = 0
        if wait_cars:
            next_car = wait_cars.popleft()
            park_car_info[parking_space] = next_car
            total_cost += cars[next_car] * park_cost[parking_space]

print(total_cost)
