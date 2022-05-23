from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    q = deque()
    for i in range(n):
        if visited[i] == False:
            q.append(i)
            answer += 1
        while(q):
            now = q.popleft()
            visited[now] = True
            for j in range(n):
                if j != now and visited[j] == False and computers[now][j] == 1:
                    q.append(j)
            
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))