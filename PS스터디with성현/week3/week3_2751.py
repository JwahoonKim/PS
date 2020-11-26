import sys
input2 = sys.stdin.readline #어떤식으로 저장되는지 check 
n = input2()
n = int(n)
graph = []

for i in range(n):
    graph.append(int(input2()))

graph.sort()

for i in range(n):
    print(graph[i])

a = 1
a = []
a = sys.stdin.readline