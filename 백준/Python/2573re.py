    import sys,copy

    sys.setrecursionlimit(10000)
    input = sys.stdin.readline

    #1년 후 녹은 빙산그래프를 리턴하는 함수
    def melt(graph):
        temp = copy.deepcopy(graph)
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for x in range(row):
            for y in range(col):
                count = 0
                if graph[x][y] == 0:
                    continue
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < row and 0 <= ny < col:
                        if graph[nx][ny] == 0:
                            count += 1
                temp[x][y] = graph[x][y] - count if graph[x][y] - count > 0 else 0
        return temp

    #(x,y)좌표부터 시작하는 빙산 한덩이가 있다면 True를 리턴하는 함수
    def countIce(graph, x, y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        if graph[x][y] != 0:
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]  
                if 0 <= nx < row and 0 <= ny < col:
                    countIce(graph, nx, ny)
            return True
        return False


    if __name__ == "__main__":
        row, col = map(int, input().split())
        graph = []
        year = 0
        for _ in range(row):
            graph.append(list(map(int, input().split())))

        while(1):
            flag = False
            count = 0
            graph = melt(graph)
            year += 1
            temp = copy.deepcopy(graph)
            for x in range(row):
                for y in range(col):
                    if countIce(temp, x, y) == True:
                        count += 1
                        if count >= 2:
                            flag = True
                            break
                if flag == True:
                    break
            if flag == True:
                break
            if count == 0:
                year = 0
                break
        print(year)

