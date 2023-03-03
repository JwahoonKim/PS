import heapq
from collections import deque


def solution(jobs):
    answer, count, cur_time = 0, 0, 0
    job_q = deque(sorted(jobs, key=lambda x: (x[0], x[1])))

    heap = []
    while count < len(jobs):
        for job in list(job_q):
            if job[0] <= cur_time:
                start_time, run_time = job_q.popleft()
                heapq.heappush(heap, [run_time, start_time])
        if not heap:
            cur_time += 1
        else:
            run_time, start_time = heapq.heappop(heap)
            answer += max(cur_time - start_time, 0)
            answer += run_time
            cur_time += run_time
            count += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))