''' 
시작 줄을 선택한 뒤 좌와 우를 확인해가면서 좌 혹은 우가 존재할 시 존재하지 않을 때까지 간다.
이때 범위를 잘 체크하자.
또 무한루프가 돌지 않는지 잘 확인하자.(좌로 가면 우가 존재하는지 확인말고 좌로 쭉가야함) 
>>> 무한루프 도는 건 지나온 길을 0으로 바꿔주면 해결되네!
'''
# 거꾸로 움직인다면 첫번째 줄에서 1인 경우 사다리를 다 타볼필요가 없네..
# 맨 마지막에 2를 찾아서 거기서부터 역사다리를 타면 더 효율적이게 풀리겠다.
T = 10
for test_case in range(1, T + 1):
    N = input()
    graph = []
    dy = [-1, 1]
    dx = 1
    for i in range(100):
        graph.append(list(map(int, input().split())))
    # 첫번째 줄 1인 곳 선택
    for i in range(100):
        if graph[0][i] == 0:
            continue
        x, y = 0, i
        while x < 100:
            if graph[x][y] == 2:
                ans = i
                break
            if y > 0 and graph[x][y - 1] == 1:  #좌 확인
                while y > 0 and graph[x][y - 1] == 1:
                    y = y + dy[0]
                x = x + dx
            elif y < 99 and graph[x][y + 1] == 1:    #우 확인
                while y < 99 and graph[x][y + 1] == 1:
                    y = y + dy[1]
                x = x + dx
            else: x = x + dx    #없으면 내려가기
    print(f'#{N} {ans}')
