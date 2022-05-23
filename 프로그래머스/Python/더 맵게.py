import heapq

# 첫 풀이


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while(1):
        if scoville[0] < K:
            if len(scoville) == 1:
                return -1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + 2 * second)
            count += 1
        else:
            return count

# 두 번째 풀이


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(scoville[0] < K):
        if len(scoville) == 1:
            return -1
        answer += 1
        mix = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, mix)
    return answer
