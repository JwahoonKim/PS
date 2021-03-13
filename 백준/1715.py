import heapq

n = int(input())
answer = 0
now = 0
numbers = []
for _ in range(n):
    heapq.heappush(numbers, int(input()))

while(len(numbers) > 1):
    # 두개 뽑고 비교 
    compare = heapq.heappop(numbers) + heapq.heappop(numbers)
    # 비교한 양 누적시키기
    answer += compare
    # 합친 숫자 묶음 다시 힙큐에 삽입
    heapq.heappush(numbers, compare)
    
print(answer)
