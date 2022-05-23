import sys, heapq
input = sys.stdin.readline

def minus(a):
    c,d = a[0], a[1]
    return -c

T = int(input())
for i in range(T):
    n = int(input())
    visited = [False] * n
    min = []
    max = []
    for i in range(n): 
        operator, num = input().split()
        num = int(num)
        if operator == "I":
            heapq.heappush(min, (num, i))
            heapq.heappush(max, (-num, i))
        else:
            if num == 1:
                while(max):
                    a = heapq.heappop(max)
                    if visited[a[1]] == False:
                        visited[a[1]] = True
                        break
            else:
                while(min):
                    a = heapq.heappop(min)
                    if visited[a[1]] == False:
                        visited[a[1]] = True
                        break

    minValue = [i[0] for i in min]
    maxValue = [-i[0] for i in max]
    result = sorted(list(set(minValue) & set(maxValue)))
    if len(result) == 0:
        print("EMPTY")
    else:
        print(result[-1], result[0])
