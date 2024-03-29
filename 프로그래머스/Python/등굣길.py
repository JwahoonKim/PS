def solution(m, n, puddles):
    answer = 0
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    dist[0][1] = 1

    for x, y in puddles:
        dist[x][y] = 'X'
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 1. 가려는 곳이 웅덩이라면 0 넣어주기
            if dist[i][j] == 'X':
                dist[i][j] = 0
            else:
                # 2. 웅덩이가 아니라면 왼쪽 + 위쪽의 합으로 저장
                left = dist[i][j - 1]
                top = dist[i - 1][j]
                dist[i][j] = left + top

    answer = dist[m][n] % 1000000007 
    return answer
