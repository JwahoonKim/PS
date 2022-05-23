from itertools import combinations as C

N = int(input())
answer = 987654321
people = [i for i in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
        
# 팀 뽑기
for team1 in list(C(people, N // 2)):
    team2 = [i for i in people if i not in team1]
        
    # 팀 별 점수 구하기
    score1 = 0
    score2 = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score1 += graph[team1[i]][team1[j]] + graph[team1[j]][team1[i]]
            score2 += graph[team2[i]][team2[j]] + graph[team2[j]][team2[i]]
    answer = min(abs(score1 - score2) , answer)
print(answer)
