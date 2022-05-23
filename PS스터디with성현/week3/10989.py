import sys
input2 = sys.stdin.readline
print2 = sys.stdout.write

n = int(input())
#sort 는 O(nlogn) 이랬는데 O(N)으로 해야됨
# -> 배열 탐색 
#N = 10000까지 자연수
graph = [0] * 10001

for i in range(n):
    num = int(input2())
    graph[num] += 1

for i in range(10001):
    if graph[i] != 0:
        for j in range(graph[i]):
            print(i)