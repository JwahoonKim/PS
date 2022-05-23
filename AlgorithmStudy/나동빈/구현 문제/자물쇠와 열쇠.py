def rotate_90_degree(key_graph):
    #graph를 90도 회전한 그래프를 리턴.
    n = len(key_graph)
    rotated_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_graph[i][j] = key_graph[n - 1 - j][i]
    return rotated_graph

def check(graph, Start, size):
    #특정 범위의 그래프값이 모두 1인지 check
    for x in range(Start, Start + size):
        for y in range(Start, Start + size):
            if graph[x][y] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    check_graph = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            check_graph[i][j] = lock[i - n][j - n]
    for rotate in range(4):
        key = rotate_90_degree(key)
        for x in range(2 * n):
            for y in range(2 * n):
                for i in range(m):
                    for j in range(m):
                        check_graph[x + i][y + j] += key[i][j]
                if check(check_graph, n, n) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        check_graph[x + i][y + j] -= key[i][j]
    return False
            


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))