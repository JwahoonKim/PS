import sys, heapq
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    minHeap = []
    maxHeap = []
    for j in range(n):
        operator, num = input().split()
        num = int(num)
        if operator == 'I':
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, -num)
        if operator == 'D':
            elif num == -1:
                heapq.heappop(minHeap)
            elif num == 1:
                heapq.heappop(maxHeap)
    maxHeap = map(lambda x : -x, maxHeap)
    result = sorted(list(set(minHeap) & set(maxHeap)))

    if len(result) == 0:
        print('EMPTY')
    else:
        print(result[-1], result[0])
            

