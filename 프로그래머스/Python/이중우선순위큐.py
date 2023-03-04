import heapq
from collections import defaultdict

INSERT = 'I'
DELETE = 'D'
MAX_DELETE = 1
MIN_DELETE = -1


def solution(operations):
    min_heap = []
    max_heap = []
    q_status = defaultdict(int)

    for operation in operations:
        op, operand = operation.split(" ")
        operand = int(operand)
        if op == INSERT:
            insert(max_heap, min_heap, operand, q_status)
        elif op == DELETE:
            delete(max_heap, min_heap, operand, q_status)

    return get_answer(max_heap, min_heap, q_status)


def get_answer(max_heap, min_heap, q_status):
    answer = [0, 0]
    while max_heap:
        n = heapq.heappop(max_heap)
        n = -n
        if q_status[n] > 0:
            answer[0] = n
            break
    while min_heap:
        n = heapq.heappop(min_heap)
        if q_status[n] > 0:
            answer[1] = n
            break
    return answer


def delete(max_heap, min_heap, operand, q_status):
    if operand == MAX_DELETE:
        delete_max_heap(max_heap, q_status)

    elif operand == MIN_DELETE:
        delete_min_heap(min_heap, q_status)


def delete_min_heap(min_heap, q_status):
    while min_heap:
        n = heapq.heappop(min_heap)
        if q_status[n] > 0:
            q_status[n] -= 1
            break


def delete_max_heap(max_heap, q_status):
    while max_heap:
        n = heapq.heappop(max_heap)
        n = -n
        if q_status[n] > 0:
            q_status[n] -= 1
            break


def insert(max_heap, min_heap, operand, q_status):
    heapq.heappush(min_heap, operand)
    heapq.heappush(max_heap, -operand)
    q_status[operand] += 1

# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
