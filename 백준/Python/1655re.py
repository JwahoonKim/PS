import heapq, sys
input = sys.stdin.readline

#heapq 최소힙
n = int(input())
left = [-int(input())]
right = []

#첫번째 중앙값 출력
print(-left[0])
flag = right
# 2 ~ n번째 중앙값 출력
#left[0]이 계속 중앙값이 되도록 만들기
for i in range(n - 1):
    number = int(input())
    if flag == right:
        heapq.heappush(flag, number)
        flag = left
    else: 
        heapq.heappush(flag, -number)
        flag = right
    
    if flag == right and -left[0] > right[0]:
        left[0], right[0] = -right[0], -left[0]
    print(-left[0])
