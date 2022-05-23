# 첫 풀이
def dfs(start, visited, computers, n):
    if visited[start] == False:
        visited[start] = True
        for i in range(n):
            if visited[i] == False:
                if computers[start][i] == 1:
                    dfs(i, visited, computers)
        return True


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if dfs(i, visited, computers) == True:
            answer += 1
    return answer

# 두 번째 풀이


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if dfs(n, computers, visited, i) == True:
            answer += 1
    return answer


def dfs(n, computers, visited, i):
    if visited[i] == True:
        return False
    else:
        for j in range(n):
            if i == j:
                continue
            else:
                if computers[i][j] == 1 and visited[j] == False:
                    dfs(n, computers, visited, j)
                    visited[j] = True
        return True
