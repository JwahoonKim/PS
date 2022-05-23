from itertools import combinations as cb

# 학생이 벽에 다 가렸는지 체크하는 함수
def isHided(graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "S":
                # 십자가 모양으로 주변을 살펴보기
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while 1:
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] == "O":
                                break
                            elif graph[nx][ny] == "T":
                                return False
                            else:
                                nx = nx + dx[k]
                                ny = ny + dy[k]
                        else:
                            break
    return True


def huboMaker(graph):
    hubo = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T":
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while 1:
                        if (
                            (0 <= nx < n and 0 <= ny < n)
                            and graph[nx][ny] != "S"
                            and graph[nx][ny] != "T"
                        ):
                            if (nx, ny) not in hubo:
                                hubo.append((nx, ny))
                            nx = nx + dx[k]
                            ny = ny + dy[k]
                        else:
                            break
    return hubo


# 입력 받기
n = int(input())
answer = "NO"
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))


# 벽을 설치할 위치 후보를 리스트로 만든다.
wallHubo = huboMaker(graph)
threeChoiceOfHubo = list(cb(wallHubo, 3))

for hubo in threeChoiceOfHubo:
    x1, y1 = hubo[0][0], hubo[0][1]
    x2, y2 = hubo[1][0], hubo[1][1]
    x3, y3 = hubo[2][0], hubo[2][1]
    # 벽 설치
    graph[x1][y1] = "O"
    graph[x2][y2] = "O"
    graph[x3][y3] = "O"
    # 벽 설치했는데 숨겨지면 answer = YES 끝
    if isHided(graph) == True:
        answer = "YES"
        break
    # 숨겨지지 않으면 다시 벽 제거하고 다음 후보벽 설치하러 ㄱㄱ
    else:
        graph[x1][y1] = "X"
        graph[x2][y2] = "X"
        graph[x3][y3] = "X"

print(answer)

