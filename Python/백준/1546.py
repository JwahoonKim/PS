n = int(input())
scores = list(map(int, input().split()))
maxi = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i] / maxi * 100
ans = sum(scores) / len(scores)
print(ans)