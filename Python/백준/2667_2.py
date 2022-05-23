n = int(input())
house = []
danzi = []
for _ in range(n):
    house.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global count
    if 0 <= x < n and 0 <= y < n:
        if house[x][y] == 1:
            house[x][y] = 0
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            count = 0
            dfs(i, j)
            danzi.append(count)
            
print(len(danzi))
for n in sorted(danzi):
    print(n)