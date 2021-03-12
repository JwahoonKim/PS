import sys, heapq
input = sys.stdin.readline

n = int(input())
answer = 0
now = 0
numbers = []
for _ in range(n):
    heapq.heappush(numbers, int(input()))


while(len(numbers) > 1):
    compare = heapq.heappop(numbers) + heapq.heappop(numbers)
    answer += compare
    heapq.heappush(numbers, compare)
print(answer)
