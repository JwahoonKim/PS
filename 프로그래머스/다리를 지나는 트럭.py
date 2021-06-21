from collections import deque

# 첫 풀이


def solution(bridge_length, weight, truck_weights):
    nowWeight = 0
    time = 0
    cur = 0
    goingTruck = deque()
    while 1:
        if cur < len(truck_weights):
            while nowWeight + truck_weights[cur] <= weight:
                # 넣는 경우
                time += 1
                for i in range(len(goingTruck)):
                    goingTruck[i][1] += 1
                goingTruck.append([truck_weights[cur], 1])
                nowWeight += truck_weights[cur]
                cur += 1
                if goingTruck[0][1] == bridge_length:
                    w, d = goingTruck.popleft()
                    nowWeight -= w
                if cur == len(truck_weights):
                    break
        # 다리에 트럭 더 못올리는 경우
        time += 1
        for i in range(len(goingTruck)):
            goingTruck[i][1] += 1
        if goingTruck[0][1] == bridge_length:
            w, d = goingTruck.popleft()
            nowWeight -= w
        if cur == len(truck_weights) and len(goingTruck) == 0:
            break
    return time + 1


bridge_length = 100
weight = 100
truck_weights = [10]

print(solution(bridge_length, weight, truck_weights))

# 두 번째 풀이


def solution(bridge_length, weight, truck_weights):
    time = 0
    now_weight = 0
    trucks = deque(truck_weights)
    bridge_status = deque()
    while(trucks or bridge_status):
        time += 1
        if(trucks and now_weight + trucks[0] <= weight):
            cur_truck = trucks.popleft()
            bridge_status.append([cur_truck, 0])
            now_weight += cur_truck
        for status in bridge_status:
            status[1] += 1
        if bridge_status[0][1] == bridge_length:
            arrival = bridge_status.popleft()
            now_weight -= arrival[0]

    return time + 1
