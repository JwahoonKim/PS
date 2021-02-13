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

