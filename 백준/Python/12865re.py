n, k = map(int, input().split())
W = []
V = []
for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]
# pick함수는 고르냐 안고르냐, i는 순번 , w는 현재 차있는 무게
def pick(i, w):
    if dp[i][w] > 0:
        return dp[i][w]
    if i == n:
        return 0
    v1 = 0
    # 고른다
    if w + W[i] <= k:
        v1 = V[i] + pick(i + 1, W[i] + w)
    # 안고른다
    v2 = 0 + pick(i + 1, w)
    dp[i][w] = max(v1, v2)
    return max(v1, v2)


answer = pick(0, 0)
print(answer)
