T = int(input())
for _ in range(T):
    n = int(input())
    answer = n
    numbers = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    for i in range(1, len(numbers)):
        if visited[i] == True:
            continue
        now = i
        team = []
        while(1):
            if visited[now] == True:
                if now in team:
                    answer -= len(team[team.index(now):])
                break
            visited[now] = True
            team.append(now)
            if now == numbers[now]:
                answer -= 1
                break
            now = numbers[now]
    print(answer)
