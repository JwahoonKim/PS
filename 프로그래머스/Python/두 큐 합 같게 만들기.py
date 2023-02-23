from collections import deque
from typing import List


def solution(queue1: List, queue2: List):
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    total_sum = q1_sum + q2_sum
    if total_sum % 2 == 1:
        return -1

    half_sum = total_sum / 2
    q1 = deque(queue1)
    q2 = deque(queue2)

    answer = 0
    for _ in range(3 * (len(queue1) + len(queue2))):
        if q1_sum == q2_sum:
            return answer
        if q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        elif q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q1_sum += num
            q2_sum -= num
        answer += 1

    return -1
