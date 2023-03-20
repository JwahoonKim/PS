import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        answer = [0] * n
        meeting_q = []

        for start, end in sorted(meetings):
            while meeting_q and meeting_q[0][0] <= start:
                _, room_number, _ = heapq.heappop(meeting_q)
                heapq.heappush(rooms, room_number)

            if rooms:
                room_number = heapq.heappop(rooms)
                answer[room_number] += 1
                heapq.heappush(meeting_q, [end, room_number, [start, end]])

            else:
                _, room_number, [pre_start, pre_end] = heapq.heappop(meeting_q)
                answer[room_number] += 1
                heapq.heappush(meeting_q, [pre_end + end - start, room_number, [pre_end, pre_end + end - start]])

        return answer.index(max(answer))


print(Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
print(Solution().mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))
print(Solution().mostBooked(4, [[12,44],[27,37],[48,49],[46,49],[24,44],[32,38],[21,49],[13,30]])) # 1

