graph = []
count = [0] * 10
for i in range(3):
    graph.append(int(input()))

result = graph[0] * graph[1] * graph[2]
result = str(result)

for i in result:
    count[int(i)] += 1
for i in count:
    print(i)