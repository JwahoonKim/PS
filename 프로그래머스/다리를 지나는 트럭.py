from collections import deque


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