N, K = map(int, input().split(" "))
info = []

gold = 0
silver = 0
bronze = 0

for _ in range(N):
    now = list(map(int, input().split(" ")))
    info.append(now)
    
    if now[0] == K:
        gold = now[1]
        silver = now[2]
        bronze = now[3]

answer = 1

for c in info:
    if c[1] > gold:
        answer += 1
    if c[1] == gold:
        if c[2] > silver:
            answer += 1
        if c[2] == silver:
            if c[3] > bronze:
                answer += 1

print(answer)
