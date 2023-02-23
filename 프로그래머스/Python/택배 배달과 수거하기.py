from collections import deque
from typing import List


def calc_to_go(del_q, pick_q):
    if not del_q:
        return pick_q[-1][0]
    if not pick_q:
        return del_q[-1][0]
    return del_q[-1][0] if del_q[-1][0] >= pick_q[-1][0] else pick_q[-1][0]


def solution(cap, n, deliveries: List, pickups: List):
    del_q = deque()
    pick_q = deque()

    for idx, delivery in enumerate(deliveries, 1):
        if delivery != 0:
            del_q.append([idx, delivery])

    for idx, pickup in enumerate(pickups, 1):
        if pickup != 0:
            pick_q.append([idx, pickup])

    answer = 0
    while del_q or pick_q:
        capacity = cap
        to_go = calc_to_go(del_q, pick_q)
        answer += 2 * to_go

        while del_q and del_q[-1][1] <= capacity:
            capacity -= del_q.pop()[1]
        if del_q:
            del_q[-1][1] -= capacity

        capacity = cap
        while pick_q and pick_q[-1][1] <= capacity:
            capacity -= pick_q.pop()[1]
        if pick_q:
            pick_q[-1][1] -= capacity

    return answer

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# print(solution(2, 4, [0,0,0,0], [1,2,3,4]))
print(solution(2, 2, [0, 0], [0, 0]))