import heapq, sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        # 원소를 음수로 넣어주면 최소힙을 최대힙처럼 구현가능
        heapq.heappush(heap, -x)