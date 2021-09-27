import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
dp = [[0] * (K + 1) for _ in range(N)]
for _ in range(N):
    W, V = map(int, input().split())
    items.append([W, V])
    
items.sort()

for i in range(K + 1):
    if i >= items[0][0]:
        dp[0][i] = items[0][1]
        
for i in range(1, N):
    W_now, V_now = items[i][0], items[i][1]
    for j in range(1, K + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        if j >= W_now:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W_now] + V_now)

print(dp[-1][-1])