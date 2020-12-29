N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
house = 0 #다른 부분★
h_list = [] #다른 부분★

def dfs(x, y):
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] == 1:
            global house #다른 부분★  글로벌 쓰기 싫은데 대안 check
            house += 1 #다른 부분★
            graph[x][y] = 0
            # for문 + 방향벡터로 하는게 더 깔끔하겠다.
            dfs(x - 1, y)
            dfs(x , y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True       
    return False

count = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            count += 1
            h_list.append(house) #다른 부분★
            house = 0 #다른 부분★ 초기화 

print(count)
a = sorted(h_list)
h_list.sort()
#프린트 다른 방법 체크
for i in h_list:
    print(i)

for i in sorted(h_list):
    print(i)    